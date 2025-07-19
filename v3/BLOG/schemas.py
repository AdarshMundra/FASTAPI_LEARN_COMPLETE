from typing import List, Optional
from pydantic import BaseModel

class BlogBase(BaseModel, from_attributes=True):
    title: str
    body: str

class Blog(BlogBase, from_attributes=True):
    pass

class User(BaseModel, from_attributes=True):
    name: str
    email: str
    password: str

class ShowUser(BaseModel, from_attributes=True):
    name: str
    email: str
    blogs: List[Blog] = []

class ShowBlog(BaseModel, from_attributes=True):
    title: str
    body: str
    creator: ShowUser

class Login(BaseModel):
    username: str
    password:str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None