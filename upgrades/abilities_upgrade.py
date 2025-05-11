class UpgradeTree:
    """Класс для управления древом улучшений способностей."""

    def __init__(self):
        """Инициализация пустого списка умений."""
        self.unlocked = []

    def unlock(self, ability: str, cost: int, currency: CurrencySystem):
        """
        Разблокирует новое умение.

        :param ability: Название умения.
        :param cost: Стоимость в красных сферах.
        :param currency: Экземпляр валютной системы.
        """
        if currency.spend_orbs(cost):
            self.unlocked.append(ability)
            print(f"Разблокировано: {ability}")

    def show(self):
        """Показывает список разблокированных умений."""
        print("Умения:")
        for ability in self.unlocked:
            print(f"- {ability}")
