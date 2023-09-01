from fastapi import FastAPI
import json

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello Baby"}


@app.get("/characters")
def get_characters():
    with open("../data/characters.json", "r") as f:
        data = json.load(f)
    return data
