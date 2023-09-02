from fastapi import FastAPI, status, HTTPException, Response
import psycopg2
from psycopg2.extras import RealDictCursor
import os
from dotenv import load_dotenv

from api_utils import (
    add_character,
    save_json,
    load_json,
    get_character_ids,
    get_character_info,
    remove_character,
    update_char,
)
from schemas.character import Character

app = FastAPI()

load_dotenv()

try:
    connection = psycopg2.connect(
        host="localhost",
        database=os.getenv("DATABASE"),
        user=os.getenv("USER"),
        password=os.getenv("PASSWORD"),
        port="5432",
        cursor_factory=RealDictCursor,
    )
    cursor = connection.cursor()
    print("Database connection was succeful")
except Exception as error:
    print("Connecting to Database failed")
    print("Error : ", error)


@app.get("/")
async def root():
    return {"message": "Hello Baby"}


@app.get("/characters")
def get_character_ids():
    id_list = get_character_ids
    return id_list


@app.get("/characters/")
def get_character(id: str):
    chara_info = get_character_info(id)
    if chara_info == 404:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"character id {id} not found"
        )
    else:
        return chara_info


@app.post("/createchar", status_code=status.HTTP_201_CREATED)
def create_char(character: Character):
    data = load_json("characters.json")
    add_character(character.model_dump(), data)
    save_json("characters.json", data)

    print(character)
    return {"new_character": character.model_dump()}


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
    print(character)
    response = update_char(id, character.model_dump())
    if response == 404:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="cannot update a non-existent id",
        )
    else:
        return {"message": "character updated"}
