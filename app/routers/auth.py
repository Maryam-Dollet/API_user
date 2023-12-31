from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.database_utils import get_db
from app.schemas.user import Token

# from schemas.user import UserLogin
from app import models, oauth2, utils

router = APIRouter(tags=["Authentication"])


@router.post("/login", response_model=Token)
def login(
    user_credentials: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db),
):
    # OAuth2PasswordRequestForm = dict(username, password)
    user = (
        db.query(models.User)
        .filter(models.User.email == user_credentials.username)
        .first()
    )

    if not user:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Invalid Credentials"
        )

    if not utils.verify(user_credentials.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Invalid Credentials"
        )

    # create token
    access_token = oauth2.create_access_token(data={"user_id": str(user.user_id)})
    # return token
    return {"access_token": access_token, "token_type": "bearer"}
