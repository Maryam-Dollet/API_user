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
def create_char(payload: dict = Character):
    with open("data/characters.json", "r") as f:
        data = json.load(f)

    add_character(payload["name"], payload["occupation"], data)

    save_json("characters.json", data)

    return {
        "new_character": f"name: {payload['name']}, occupation: {payload['occupation']}"
    }
