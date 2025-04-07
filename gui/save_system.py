import json
import os

SAVE_FILE = "savegame.json"

def save_game(data):
    with open(SAVE_FILE, "w") as f:
        json.dump(data, f)
    print("Игра сохранена.")

def load_game():
    if os.path.exists(SAVE_FILE):
        with open(SAVE_FILE, "r") as f:
            return json.load(f)
    else:
        print("Сохранений не найдено.")
        return None