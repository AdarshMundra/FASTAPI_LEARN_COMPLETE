# BLOG/routers/blog.py
from database import get_db
import models, schemas

from fastapi import APIRouter, Depends,HTTPException,status
from sqlalchemy.orm import Session

router = APIRouter(prefix="/blogs",tags=['Blogs'])


@router.get('')
def all(db:Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs


@router.get('/{id}')
def show(id, db:Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        return f"Blog with id {id} is not present"
    return blog

@router.put('/{id}')
def update(id:int, request: schemas.Blog, db:Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Blog with id {id} not found")
    blog.update(request.dict())
    db.commit()
    return 'updated successfully'


@router.delete('/{id}')
def destroy(id:int,db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)

    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Blog with id {id} not found")

    blog.delete(synchronize_session=False)
    db.commit()
    return 'done'

@router.post('')
def create_blog(request: schemas.Blog, db:Session = Depends(get_db)):
    new_blog = models.Blog(title=request.title, body=request.body,user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

