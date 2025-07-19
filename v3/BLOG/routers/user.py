from database import get_db
import schemas
from fastapi import APIRouter, Depends,status
from sqlalchemy.orm import Session
from code_repo import user_code

router = APIRouter(prefix="/users",tags=['users'])


@router.post('/create',response_model=schemas.ShowUser, status_code=status.HTTP_201_CREATED)
def create_user(request: schemas.User,db: Session = Depends(get_db)):
    return user_code.create_user(request, db)

@router.get('/')
def all_users(db: Session = Depends(get_db)):
    return user_code.all_users(db)

@router.get('/{id}', response_model=schemas.ShowUser)
def get_user(id:int, db: Session = Depends(get_db)):
    return user_code.get_single_user(id, db)