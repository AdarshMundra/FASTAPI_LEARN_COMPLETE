# BLOG/routers/blog.py
from database import get_db
import schemas,oauth2
from code_repo import blog_code
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

router = APIRouter(prefix="/blogs",tags=['Blogs'])


@router.get('')
def all(db:Session = Depends(get_db),current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog_code.get_all(db)


@router.get('/{id}')
def show(id, db:Session = Depends(get_db),current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog_code.single_record(id, db)

@router.put('/{id}')
def update(id:int, request: schemas.Blog, db:Session = Depends(get_db),current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog_code.update_record(id, request, db)

@router.delete('/{id}')
def destroy(id:int,db: Session = Depends(get_db),current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog_code.delete_record(id, db)

@router.post('')
def create_blog(request: schemas.Blog, db:Session = Depends(get_db),current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog_code.create_record(request, db)

