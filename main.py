from fastapi import FastAPI
from typing import Optional

app = FastAPI()

@app.get("/")
def read_root():
    return {"data":"Blog list"}

@app.get("/blog")
def blog(limit:int =10,published:bool = True, sort : Optional['str']=None):
    if published:
        return {"data":f"{limit} blog from Published Blog list"}  
    return {"data":f"{limit} blog from Unpublished Blog list"}

@app.get("/blog/unpublished")
def blog():
    return {"data":"Blog list"}

@app.get("/blog/{id}")
def blog(id:int):
    return {"data":id}

@app.get("/blog/{id}/comments")
def blog(id:int):
    return {"data":[1,2]}
