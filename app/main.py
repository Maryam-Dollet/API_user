from fastapi import FastAPI, status, HTTPException, Response, Depends
from sqlalchemy.orm import Session
from sqlalchemy import exc
from schemas.character import CharacterBase, CharacterResponse
import models
from database_utils import engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello Baby"}


@app.get("/characters")
def get_character_id(db: Session = Depends(get_db)):
    character_id_list = db.query(models.Character.character_id).all()
    return [x[0] for x in character_id_list]


@app.get("/characters/", response_model=CharacterResponse)
def get_character(id: str, db: Session = Depends(get_db)):
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


@app.post(
    "/createchar", status_code=status.HTTP_201_CREATED, response_model=CharacterResponse
)
def create_char(character: CharacterBase, db: Session = Depends(get_db)):
    # ** unpack the dictionary
    new_character = models.Character(**character.model_dump())
    db.add(new_character)
    db.commit()
    db.refresh(new_character)
    return new_character


@app.delete("/characters/", status_code=status.HTTP_204_NO_CONTENT)
def delete_character(id: str, db: Session = Depends(get_db)):
    try:
        character = db.query(models.Character).filter(
            models.Character.character_id == id
        )

        if character.first() == None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="cannot delete a non-existent id",
            )

        character.delete(synchronize_session=False)
        db.commit()

        return Response(status_code=status.HTTP_204_NO_CONTENT)
    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)


@app.put("/characters/", response_model=CharacterResponse)
def update_character(id: str, character: CharacterBase, db: Session = Depends(get_db)):
    try:
        character_query = db.query(models.Character).filter(
            models.Character.character_id == id
        )

        updated_character = character_query.first()

        if updated_character == None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="cannot delete a non-existent id",
            )

        if character.age == None:
            character_info = character.model_dump(exclude="age")
        else:
            character_info = character.model_dump()

        character_query.update(character_info, synchronize_session=False)
        db.commit()

        return character_query.first()
    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
