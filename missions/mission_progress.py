import time

class MissionProgress:
    """Класс для отслеживания прогресса выполнения миссии."""

    def __init__(self, goal: str, time_limit: int):
        """
        Инициализация миссии.

        :param goal: Цель миссии.
        :param time_limit: Ограничение по времени в секундах.
        """
        self.goal = goal
        self.time_limit = time_limit
        self.start_time = None

    def start(self):
        """Запускает таймер миссии."""
        self.start_time = time.time()
        print("Миссия началась.")

    def check_goal(self, state: dict) -> bool:
        """
        Проверяет, достигнута ли цель миссии.

        :param state: Текущее состояние миссии.
        :return: True, если цель выполнена, иначе False.
        """
        if state.get("boss_defeated"):
            print("Цель выполнена!")
            return True
        print("Цель ещё не выполнена.")
        return False
