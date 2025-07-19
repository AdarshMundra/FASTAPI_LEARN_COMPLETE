from fastapi import HTTPException,status
import schemas, models, hashing

def create_user(request,db):
    hashedPassword = hashing.Hash.bcrypt(request.password)
    user= models.User(name=request.name, email=request.email, password=hashedPassword)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def all_users(db):
    return db.query(models.User).all()

def get_single_user(id, db):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with id {id} is not available")
    return user
