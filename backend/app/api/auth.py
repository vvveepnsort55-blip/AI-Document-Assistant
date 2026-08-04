from fastapi import APIRouter, HTTPException


from database import SessionLocal


# Models
from models.user import User


# Schemas
from schemas.user import UserCreate, UserLogin


# Security
from core.security import (
    hash_password,
    verify_password,
    create_access_token
)


router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)



@router.post("/register")
async def register(
    user: UserCreate
):

    db = SessionLocal()


    existing_user = db.query(
        User
    ).filter(
        User.email == user.email
    ).first()


    if existing_user:

        raise HTTPException(
            status_code=400,
            detail="Email already registered"
        )


    new_user = User(
        username=user.username,
        email=user.email,
        hashed_password=hash_password(
            user.password
        )
    )


    db.add(
        new_user
    )

    db.commit()

    db.refresh(
        new_user
    )


    return {
        "message": "User created successfully",
        "user_id": new_user.id
    }




@router.post("/login")
async def login(
    user: UserLogin
):

    db = SessionLocal()


    db_user = db.query(
        User
    ).filter(
        User.email == user.email
    ).first()


    if not db_user:

        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )



    if not verify_password(
        user.password,
        db_user.hashed_password
    ):

        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )



    token = create_access_token(
        {
            "sub": str(db_user.id)
        }
    )


    return {
        "access_token": token,
        "token_type": "bearer"
    }
