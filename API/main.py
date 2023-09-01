from fastapi import FastAPI
from fastapi.params import Body
import json

from api_utils import add_character, save_json
from schemas.character import Character

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello Baby"}


@app.get("/characters")
def get_character_id():
    with open("data/characters.json", "r") as f:
        data = json.load(f)
    return list(data.keys())


@app.post("/createchar")
def create_char(character: Character):
    with open("data/characters.json", "r") as f:
        data = json.load(f)

    add_character(character.name, character.occupation, data)

    save_json("characters.json", data)
    print(character)
    print(character.model_dump())
    return {
        "new_character": f"name: {character.name}, occupation: {character.occupation}"
    }
