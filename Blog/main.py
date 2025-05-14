from fastapi import FastAPI 
import schemas
# from . import schemas
import uvicorn


app = FastAPI()



@app.get('/')
def index():
    return {'data': {'name': 'Blog List'}}

@app.post('/blog')
def create_blog(request: schemas.Blog):
    return {'data': f"Blog is created with title as {request.title}"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)