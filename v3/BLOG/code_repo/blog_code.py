import models
from fastapi import HTTPException, status


def get_all(db):
    blogs = db.query(models.Blog).all()
    return blogs


def single_record(id, db):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        return f"Blog with id {id} is not present"
    return blog


def update_record(id, request, db):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Blog with id {id} not found")
    blog.update(request.dict())
    db.commit()
    return 'updated successfully'


def delete_record(id, db):
    blog = db.query(models.Blog).filter(models.Blog.id == id)

    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Blog with id {id} not found")

    blog.delete(synchronize_session=False)
    db.commit()
    return 'done'

def create_record(request,db):
    new_blog = models.Blog(title=request.title, body=request.body,user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog
