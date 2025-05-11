class PlayerProgress:
    """Класс для отображения прогресса игрока."""

    def __init__(self, level: int, difficulty: str, completion: float):
        """
        Инициализирует объект прогресса игрока.

        :param level: Текущий уровень игрока.
        :param difficulty: Уровень сложности.
        :param completion: Процент завершения кампании.
        """
        self.level = level
        self.difficulty = difficulty
        self.completion = completion

    def display(self):
        """Отображает текущий прогресс игрока."""
        print(f"Уровень: {self.level}")
        print(f"Сложность: {self.difficulty}")
        print(f"Прогресс: {self.completion}%")