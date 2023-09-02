import uuid
import json
from fastapi import status

from database_utils import db_connection

cursor_dict, cursor_real_dict = db_connection()


def load_json(filename: str):
    with open(f"data/{filename}", "r") as f:
        data = json.load(f)
    return data


def save_json(filename: str, data: dict | list):
    with open(f"data/{filename}", "w") as f:
        json.dump(data, f)


def get_character_ids():
    data = load_json("characters.json")
    return list(data.keys())


def get_character_info(id):
    data = load_json("characters.json")
    try:
        return data[id]
    except:
        return status.HTTP_404_NOT_FOUND


def add_character(character_info, char_list: list):
    id = uuid.uuid1()
    char_list[str(id)] = character_info


def remove_character(id):
    data = load_json("characters.json")
    try:
        del data[id]
        save_json("characters.json", data)
        return status.HTTP_204_NO_CONTENT
    except:
        return status.HTTP_404_NOT_FOUND


def update_char(id, update_info):
    data = load_json("characters.json")
    try:
        data[id] = update_info
        save_json("characters.json", data)
        return status.HTTP_202_ACCEPTED
    except:
        return status.HTTP_404_NOT_FOUND
