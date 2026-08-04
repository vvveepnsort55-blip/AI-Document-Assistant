from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from jose import jwt, JWTError

from app.database import SessionLocal
from app.models import User

from core.security import SECRET_KEY, ALGORITHM



security = HTTPBearer()



def get_token(
    credentials: HTTPAuthorizationCredentials = Depends(security)
):

    token = credentials.credentials

    print("RAW TOKEN:", token)

    return token





def get_current_user(
    token: str = Depends(get_token)
):

    print("TOKEN RECEIVED:", token)


    try:

        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )


        user_id = payload.get("sub")


        if user_id is None:

            raise HTTPException(
                status_code=401,
                detail="Invalid token"
            )


    except JWTError as e:

        print("JWT ERROR:", e)

        raise HTTPException(
            status_code=401,
            detail="Invalid token"
        )



    db = SessionLocal()


    user = db.query(
        User
    ).filter(
        User.id == int(user_id)
    ).first()



    if not user:

        raise HTTPException(
            status_code=404,
            detail="User not found"
        )


    return user
