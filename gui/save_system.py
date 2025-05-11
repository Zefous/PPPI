import json
import os

class SaveSystem:
    """Класс для управления системой сохранений игры."""

    SAVE_FILE = "savegame.json"

    def save(self, data: dict):
        """
        Сохраняет данные игры в файл.

        :param data: Словарь с данными состояния игры.
        """
        with open(self.SAVE_FILE, "w") as f:
            json.dump(data, f)
        print("Игра сохранена.")

    def load(self) -> dict:
        """
        Загружает данные игры из файла.

        :return: Словарь с сохранёнными данными или пустой словарь.
        """
        if os.path.exists(self.SAVE_FILE):
            with open(self.SAVE_FILE, "r") as f:
                return json.load(f)
        print("Сохранения не найдены.")
        return {}