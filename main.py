from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"data":"Blog list"}

@app.get("/blog")
def blog():
    return {"data":"Blog list"}

@app.get("/blog/unpublished")
def blog():
    return {"data":"Blog list"}

@app.get("/blog/{id}")
def blog(id:int):
    return {"data":id}

@app.get("/blog/{id}/comments")
def blog(id:int):
    return {"data":[1,2]}
