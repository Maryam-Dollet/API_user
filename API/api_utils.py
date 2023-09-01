import uuid
import json


def add_character(character_info, char_list: list):
    id = uuid.uuid1()
    char_list[str(id)] = character_info


def get_character_ids():
    data = load_json("characters.json")
    return list(data.keys())


def get_character_info(id):
    data = load_json("characters.json")
    return data[id]


def load_json(filename: str):
    with open(f"data/{filename}", "r") as f:
        data = json.load(f)
    return data


def save_json(filename: str, data: dict | list):
    with open(f"data/{filename}", "w") as f:
        json.dump(data, f)
