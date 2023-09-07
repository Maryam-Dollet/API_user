from jose import JWTError, jwt
from fastapi import Depends, status, HTTPException
from fastapi.security import OAuth2PasswordBearer
from dotenv import load_dotenv
import os
from app import models
from datetime import datetime, timedelta
from app.schemas.user import TokenData
from sqlalchemy.orm import Session
from app.database_utils import get_db

# from config import settings

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

load_dotenv()

# generate secret key : openssl rand -hex 32
SECRET_KEY = os.getenv("SECRET_KEY")
# Algorithm
ALGORITHM = os.getenv("ALGORITHM")
# Expiration time
ACCESS_TOKEN_EXPIRE_MINUTES = os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES")


def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=int(ACCESS_TOKEN_EXPIRE_MINUTES))

    to_encode.update({"exp": expire})

    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return encoded_jwt


def verify_access_token(token: str, credentials_exception):
    try:
        payload = jwt.decode(token, SECRET_KEY, [ALGORITHM])

        id: str = payload.get("user_id")

        if id is None:
            raise credentials_exception

        token_data = TokenData(user_id=id)
    except JWTError:
        raise credentials_exception

    return token_data


def get_current_user(
    token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)
):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    token = verify_access_token(token, credentials_exception)
    user = db.query(models.User).filter(models.User.user_id == token.user_id).first()
    # print(user)

    # return verify_access_token(token, credentials_exception)
    return user
