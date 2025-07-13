from fastapi import FastAPI, Request , Depends, status,HTTPException
import uvicorn, schemas,models, hashing
from sqlalchemy.orm import Session
from database import engine , SessionLocal

models.Base.metadata.create_all(engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()





app = FastAPI()

@app.get('/')
def index():
    return {'data': {'name': 'Blog List'}}


@app.post('/create',response_model=schemas.ShowUser, status_code=status.HTTP_201_CREATED,tags=['users'])
def create_user(request: schemas.User,db: Session = Depends(get_db)):
    hashedPassword = hashing.Hash.bcrypt(request.password)
    user= models.User(name=request.name, email=request.email, password=hashedPassword)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

@app.get('/user/',tags=['users'])
def all_users(db: Session = Depends(get_db)):
    return db.query(models.User).all()

@app.get('/user/{id}', response_model=schemas.ShowUser,tags=['users'])
def get_user(id:int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with id {id} is not available")
    return user


@app.get('/blog',tags=['Blogs'])
def all(db:Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs


@app.get('/blog/{id}',tags=['Blogs'])
def show(id, db:Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        return f"Blog with id {id} is not present"
    return blog

@app.put('/blog/{id}',tags=['Blogs'])
def update(id:int, request: schemas.Blog, db:Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Blog with id {id} not found")
    blog.update(request.dict())
    db.commit()
    return 'updated successfully'


@app.delete('/blog/{id}',tags=['Blogs'])
def destroy(id:int,db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)

    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Blog with id {id} not found")

    blog.delete(synchronize_session=False)
    db.commit()
    return 'done'

@app.post('/blog',tags=['Blogs'])
def create_blog(request: schemas.Blog, db:Session = Depends(get_db)):
    new_blog = models.Blog(title=request.title, body=request.body,user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)