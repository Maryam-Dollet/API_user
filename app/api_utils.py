import uuid
import json
from fastapi import status

from database_utils import db_connection

connection, cursor_dict, cursor_real_dict = db_connection()


def load_json(filename: str):
    with open(f"data/{filename}", "r") as f:
        data = json.load(f)
    return data


def save_json(filename: str, data: dict | list):
    with open(f"data/{filename}", "w") as f:
        json.dump(data, f)


def get_character_ids():
    cursor_dict.execute("""SELECT character_id FROM characters """)
    characters = cursor_dict.fetchall()

    character_list = []
    for x in range(len(characters)):
        character_list.append([x for x in characters[x]][0])

    return character_list


def find_character(id):
    try:
        query = "SELECT * FROM characters WHERE character_id = %s"
        cursor_real_dict.execute(query, (id,))
        character = cursor_real_dict.fetchone()
        if character == None:
            return status.HTTP_404_NOT_FOUND
        else:
            return character
    except:
        connection.rollback()
        return status.HTTP_404_NOT_FOUND


def add_character(character_info):
    try:
        cursor_real_dict.execute(
            """ INSERT INTO characters (name, occupation, age) VALUES (%s, %s, %s) RETURNING *""",
            (
                character_info["name"],
                character_info["occupation"],
                character_info["age"],
            ),
        )
        new_post = cursor_real_dict.fetchone()
        connection.commit()
        return new_post
    except:
        return status.HTTP_404_NOT_FOUND


def remove_character(id):
    query = "DELETE FROM characters WHERE character_id = %s RETURNING *"
    cursor_real_dict.execute(query, (id,))
    deleted_character = cursor_real_dict.fetchone()
    connection.commit()
    if deleted_character == None:
        return status.HTTP_404_NOT_FOUND
    else:
        return status.HTTP_204_NO_CONTENT


def update_char(id, update_info):
    data = load_json("characters.json")
    try:
        data[id] = update_info
        save_json("characters.json", data)
        return status.HTTP_202_ACCEPTED
    except:
        return status.HTTP_404_NOT_FOUND
