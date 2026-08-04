from sqlalchemy.orm import Session

from models.user import User
from schemas.user import UserRegister
from auth import hash_password


class AuthService:

    def __init__(self, db: Session):
        self.db = db

    def register(self, user: UserRegister):

        existing_user = (
            self.db.query(User)
            .filter(User.email == user.email)
            .first()
        )

        if existing_user:
            raise ValueError("Email already exists")

        new_user = User(
            username=user.username,
            email=user.email,
            hashed_password=hash_password(user.password)
        )

        self.db.add(new_user)
        self.db.commit()
        self.db.refresh(new_user)

        return new_user
