class LevelLoader:
    """Класс для загрузки уровней игрового мира."""

    def load(self, level_name: str) -> dict:
        """
        Загружает указанный уровень.

        :param level_name: Название уровня.
        :return: Словарь с информацией о статусе загрузки.
        """
        print(f"Загрузка уровня: {level_name}...")
        return {"status": "загружено", "level": level_name}
