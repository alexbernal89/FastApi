from fastapi import APIRouter, Depends, HTTPException, Path
from passlib.context import CryptContext
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session
from typing import Annotated
from starlette import status
from ..models import Todos, Users
from ..database import SessionLocal
from .auth import get_current_user

router = APIRouter(prefix='/users',
                   tags=['users']
                   )


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
class UserRequest(BaseModel):
    old_password: str
    password: str
    role: str

class UserRequestPhone(BaseModel):
    phone_number: str


bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')
db_dependency = Annotated[Session, Depends(get_db)]
user_dependency = Annotated[dict, Depends(get_current_user)]

@router.get("/user_description")
async def read_all(user: user_dependency,
                   db: db_dependency):
    if user is None:
        raise HTTPException(status_code=401, detail='Authentication Failed')
    return db.query(Users).filter(Users.id == user.get('id')).first()

@router.put("/", status_code=status.HTTP_204_NO_CONTENT)
async def update_user(user: user_dependency,
                      db: db_dependency,
                      user_request: UserRequest):
    if user is None:
        raise HTTPException(status_code=401, detail='Authentication Failed')

    user_model = db.query(Users).filter(Users.id == user.get('id')).first()
    if user_model is None:
        raise HTTPException( status_code=404, detail="Todo not found" )
    if not bcrypt_context.verify(user_request.old_password, user_model.hashed_password):
        raise HTTPException( status_code=401, detail="Error on password change" )
    user_model.hashed_password = bcrypt_context.hash(user_request.password)
    user_model.role = user_request.role
    db.add(user_model)
    db.commit()

@router.put("/update_phone", status_code=status.HTTP_204_NO_CONTENT)
async def update_phone_number(user: user_dependency,
                      db: db_dependency,
                      user_request: UserRequestPhone):
    if user is None:
        raise HTTPException(status_code=401, detail='Authentication Failed')
    user_model = db.query(Users).filter(Users.id == user.get('id')).first()
    user_model.phone_number = user_request.phone_number
    db.add(user_model)
    db.commit()

