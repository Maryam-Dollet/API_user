from fastapi import FastAPI, status, HTTPException, Response

from api_utils import (
    add_character,
    save_json,
    load_json,
    get_character_ids,
    find_character,
    remove_character,
    update_char,
)
from schemas.character import Character

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello Baby"}


@app.get("/characters")
def get_character_id():
    return {"data": get_character_ids()}


@app.get("/characters/")
def get_character(id):
    chara_info = find_character(id)
    if chara_info == 404:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"character id {id} not found"
        )
    else:
        return chara_info


@app.post("/createchar", status_code=status.HTTP_201_CREATED)
def create_char(character: Character):
    # print(character.model_dump())
    message = add_character(character.model_dump())
    return {"message": message}


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
