from fastapi import FastAPI, status, HTTPException, Response, Depends
from sqlalchemy.orm import Session

from api_utils import (
    add_character,
    find_character,
    remove_character,
    update_char,
)
from schemas.character import Character
import models
from database_utils import engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello Baby"}


@app.get("/sqlalchemy")
def test_character(db: Session = Depends(get_db)):
    characters = db.query(models.Character).all()
    return {"data": characters}


@app.get("/characters")
def get_character_id(db: Session = Depends(get_db)):
    character_id_list = db.query(models.Character.character_id).all()
    return {"data": [x[0] for x in character_id_list]}


@app.get("/characters/")
def get_character(id: str, db: Session = Depends(get_db)):
    character_info = (
        db.query(models.Character).filter(models.Character.character_id == id).first()
    )
    return character_info


@app.post("/createchar", status_code=status.HTTP_201_CREATED)
def create_char(character: Character, db: Session = Depends(get_db)):
    # ** unpack the dictionary
    new_character = models.Character(**character.model_dump())
    db.add(new_character)
    db.commit()
    db.refresh(new_character)
    return {"message": new_character}


@app.delete("/characters/", status_code=status.HTTP_204_NO_CONTENT)
def delete_character(id: str):
    response = remove_character(id)
    if response == 404:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="cannot delete a non-existent id",
        )
    else:
        return Response(status_code=status.HTTP_204_NO_CONTENT)


@app.put("/characters/")
def update_character(id: str, character: Character):
    response = update_char(id, character.model_dump())
    if response == 404:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="cannot update a non-existent id",
        )
    else:
        return {"message": response}
