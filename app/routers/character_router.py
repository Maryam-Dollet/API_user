from fastapi import status, HTTPException, Response, Depends, APIRouter
from typing import List, Optional
from sqlalchemy.orm import Session
from sqlalchemy import exc, func
from schemas.character import CharacterBase, CharacterResponse, CharacterOut
from database_utils import get_db
from utils import is_valid_uuid
import models, oauth2

router = APIRouter(tags=["Characters"])


# @router.get("/characters/all_characters", response_model=List[CharacterResponse])
# @router.get("/characters/all_characters", response_model=List[CharacterOut])
@router.get("/characters/all_characters", response_model=List[CharacterOut])
def get_characters(
    db: Session = Depends(get_db),
    current_user: str = Depends(oauth2.get_current_user),
    limit: int = 10,
    skip: int = 0,
    search: Optional[str] = "",
):
    # print(limit)s
    character_list = (
        db.query(models.Character)
        .filter(models.Character.name.contains(search))
        .limit(limit)
        .offset(skip)
        .all()
    )
    results = (
        db.query(models.Character, func.count(models.Vote.character_id).label("votes"))
        .join(
            models.Vote,
            models.Vote.character_id == models.Character.character_id,
            isouter=True,
        )
        .group_by(models.Character.character_id)
        .all()
    )
    print(results)

    return results


@router.get("/characters")
def get_character_id(
    db: Session = Depends(get_db), current_user: str = Depends(oauth2.get_current_user)
):
    character_id_list = db.query(models.Character.character_id).all()
    return [x[0] for x in character_id_list]


@router.get("/characters/", response_model=CharacterResponse)
def get_character(
    id: str,
    db: Session = Depends(get_db),
    current_user: str = Depends(oauth2.get_current_user),
):
    try:
        character_info = (
            db.query(models.Character)
            .filter(models.Character.character_id == id)
            .first()
        )
        if not character_info:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
            )
        return character_info
    except (Exception, exc.SQLAlchemyError) as error:
        # raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"{error}")
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)


@router.post(
    "/createchar", status_code=status.HTTP_201_CREATED, response_model=CharacterResponse
)
def create_char(
    character: CharacterBase,
    db: Session = Depends(get_db),
    current_user: str = Depends(oauth2.get_current_user),
):
    # print(current_user.user_id)
    # ** unpack the dictionary
    new_character = models.Character(
        **character.model_dump(), user_id=current_user.user_id
    )
    db.add(new_character)
    db.commit()
    db.refresh(new_character)
    return new_character


@router.delete("/characters/", status_code=status.HTTP_204_NO_CONTENT)
def delete_character(
    id: str,
    db: Session = Depends(get_db),
    current_user: str = Depends(oauth2.get_current_user),
):
    if not is_valid_uuid(id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="cannot delete a non-existent id",
        )

    character_query = db.query(models.Character).filter(
        models.Character.character_id == id
    )

    character = character_query.first()
    print(character.character_id)

    if character == None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="cannot delete a non-existent id",
        )

    if character.user_id != current_user.user_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Not Authorized"
        )

    character_query.delete(synchronize_session=False)
    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.put("/characters/", response_model=CharacterResponse)
def update_character(
    id: str,
    character: CharacterBase,
    db: Session = Depends(get_db),
    current_user: str = Depends(oauth2.get_current_user),
):
    if not is_valid_uuid(id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="cannot update a non-existent id",
        )

    character_query = db.query(models.Character).filter(
        models.Character.character_id == id
    )

    updated_character = character_query.first()

    if updated_character == None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="cannot update a non-existent id",
        )

    if updated_character.user_id != current_user.user_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Not Authorized"
        )

    if character.age == None:
        character_info = character.model_dump(exclude="age")
    else:
        character_info = character.model_dump()

    character_query.update(character_info, synchronize_session=False)
    db.commit()

    return character_query.first()
