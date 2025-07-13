from fastapi import FastAPI, Request , Depends, status,HTTPException
import uvicorn 
import schemas,models, hashing
from sqlalchemy.orm import Session
from database import engine , get_db
from routers import blog,user


models.Base.metadata.create_all(engine)







app = FastAPI()
app.include_router(blog.router)
app.include_router(user.router)

@app.get('/')
def index():
    return {'data': {'name': 'Blog List'}}


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)