from fastapi import FastAPI, Response, status, HTTPException

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
def get_character(id: str, response: Response):
    chara_info = get_character_info(id)
    if chara_info == 404:
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {"message": f"character id {id} not found"}
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"character id {id} not found"
        )
    else:
        return chara_info


@app.post("/createchar")
def create_char(character: Character):
    data = load_json("characters.json")
    add_character(character.model_dump(), data)
    save_json("characters.json", data)

    print(character)
    return {"new_character": character.model_dump()}
