from fastapi import FastAPI
import json

from api_utils import create_character, save_json

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello Baby"}


@app.get("/characters")
def get_character_id():
    with open("../data/characters.json", "r") as f:
        data = json.load(f)
    return list(data.keys())
