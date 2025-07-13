from database import get_db
import models, schemas,hashing

from fastapi import APIRouter, Depends,HTTPException,status
from sqlalchemy.orm import Session

router = APIRouter(prefix="/users",tags=['users'])


@router.post('/create',response_model=schemas.ShowUser, status_code=status.HTTP_201_CREATED)
def create_user(request: schemas.User,db: Session = Depends(get_db)):
    hashedPassword = hashing.Hash.bcrypt(request.password)
    user= models.User(name=request.name, email=request.email, password=hashedPassword)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

@router.get('/')
def all_users(db: Session = Depends(get_db)):
    return db.query(models.User).all()

@router.get('/{id}', response_model=schemas.ShowUser)
def get_user(id:int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with id {id} is not available")
    return user
