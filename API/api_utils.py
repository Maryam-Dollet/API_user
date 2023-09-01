import uuid
import json


def create_character(name: str, occupation: str, char_list: list):
    id = uuid.uuid1()
    character = {"name": name, "occupation": occupation}
    char_list[str(id)] = character


def save_json(filename: str, data: dict | list):
    with open(f"../data/{filename}", "w") as f:
        json.dump(data, f)
