from jose import JOSEError, jwt
from dotenv import load_dotenv
import os
from datetime import datetime, timedelta

load_dotenv()

# generate secret key : openssl rand -hex 32
SECRET_KEY = os.getenv("SECRET_KEY")
# Algorithm
ALGORITHM = os.getenv("ALGORITHM")
# Expiration time
ACCESS_TOKEN_EXPIRE_MINUTES = os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES")


def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.now() + timedelta(minutes=int(ACCESS_TOKEN_EXPIRE_MINUTES))

    to_encode.update({"exp": expire})

    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return encoded_jwt
