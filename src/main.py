import json
import os

DATA_FILE = "data/songs.json"

def load_songs():
    if not os.path.exists(DATA_FILE):
        return []

    with open(DATA_FILE, "r", encoding="utf-8") as file:
        return json.load(file)

def save_songs(songs):
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(songs, file, indent=4)


