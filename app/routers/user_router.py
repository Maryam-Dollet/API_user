from fastapi import status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from schemas.user import UserCreate, UserOut
from database_utils import get_db
import models

router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=UserOut)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    # hash the password
    user.password = hash(user.password)

    new_user = models.User(**user.model_dump())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@router.get("/{id}", response_model=UserOut)
def get_user(id: str, db: Session = Depends(get_db)):
    try:
        user = db.query(models.User).filter(models.User.user_id == id).first()

        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="cannot access a non-existent user",
            )

        return user
    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
