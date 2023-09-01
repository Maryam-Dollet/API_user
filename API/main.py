from fastapi import FastAPI

from api_utils import (
    add_character,
    save_json,
    load_json,
    get_character_ids,
    get_character_info,
)
from schemas.character import Character

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello Baby"}


@app.get("/characters")
def get_character_ids():
    id_list = get_character_ids
    return id_list


@app.get("/characters/")
def get_character(id):
    chara_info = get_character_info(id)
    return {"id_request": chara_info}


@app.post("/createchar")
def create_char(character: Character):
    data = load_json("characters.json")
    add_character(character.model_dump(), data)
    save_json("characters.json", data)

    print(character)
    # print(character.model_dump())
    return {"new_character": character.model_dump()}
