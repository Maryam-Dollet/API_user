from fastapi import FastAPI
from fastapi.params import Body
import json

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello Baby"}


@app.get("/characters")
def get_character_id():
    with open("../data/characters.json", "r") as f:
        data = json.load(f)
    return list(data.keys())


@app.post("/createchar")
def create_char(payload: dict = Body(...)):
    print(payload)
    return {
        "new_character": f"name: {payload['name']}, occupation: {payload['occupation']}"
    }
