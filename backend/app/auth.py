from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel

from sqlalchemy.orm import Session

from database import SessionLocal
from models import User

from core.security import create_access_token

from passlib.context import CryptContext



router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)



pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)




class LoginRequest(BaseModel):

    email: str

    password: str





@router.post("/login")
def login(
    data: LoginRequest
):


    db = SessionLocal()



    user = db.query(
        User
    ).filter(
        User.email == data.email
    ).first()



    if not user:

        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )



    if not pwd_context.verify(
        data.password,
        user.password
    ):

        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )



    token = create_access_token(
        {
            "sub": str(user.id)
        }
    )



    return {

        "access_token": token,

        "token_type": "bearer"

    }
