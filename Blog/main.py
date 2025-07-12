from fastapi import FastAPI , Depends , HTTPException, status
import schemas,models
from sqlalchemy.orm import Session
from database import engine , SessionLocal
# from . import schemas
import uvicorn


app = FastAPI()



models.Base.metadata.create_all(engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get('/')
def index():
    return {'data': {'name': 'Blog List'}}

@app.get('/blog')
def all(db:Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs

@app.get('/blog/unpublished')
def show(db:Session = Depends(get_db)):
    blogs = db.query(models.Blog).filter(models.Blog.published == False).all()
    return blogs

@app.get('/blog/{id}')
def show(id, db:Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        return f"Blog with id {id} is not present"
    return blog

@app.put('/blog/{id}')
def update(id:int, request: schemas.Blog, db:Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Blog with id {id} not found")
    blog.update(request.dict())
    db.commit()
    return 'updated successfully'


@app.delete('/blog/{id}')
def destroy(id:int,db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)

    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Blog with id {id} not found")

    blog.delete(synchronize_session=False)
    db.commit()
    return 'done'

@app.post('/blog')
def create_blog(request: schemas.Blog, db:Session = Depends(get_db)):
    new_blog = models.Blog(title=request.title, body=request.body,published = request.published)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

    # return {'data': f"Blog is created with title as {request.title}"}



if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)