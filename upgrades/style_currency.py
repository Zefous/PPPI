class CurrencySystem:
    """Класс для управления валютой: красные сферы и очки стиля."""

    def __init__(self):
        """Инициализация начальных значений валюты."""
        self.red_orbs = 0
        self.style_points = 0

    def add_orbs(self, amount: int):
        """Добавляет указанное количество красных сфер."""
        self.red_orbs += amount
        print(f"+{amount} красных сфер")

    def add_style_points(self, amount: int):
        """Добавляет очки стиля."""
        self.style_points += amount
        print(f"+{amount} очков стиля")

    def spend_orbs(self, cost: int) -> bool:
        """
        Пытается потратить красные сферы.

        :param cost: Стоимость покупки.
        :return: True, если покупка успешна.
        """
        if self.red_orbs >= cost:
            self.red_orbs -= cost
            return True
        print("Недостаточно сфер.")
        return False
