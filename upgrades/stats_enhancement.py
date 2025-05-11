class PlayerStats:
    """Класс для улучшения параметров персонажа."""

    def __init__(self):
        """Инициализация базовых характеристик."""
        self.hp = 100
        self.devil_energy = 50

    def upgrade_hp(self, amount: int):
        """Увеличивает уровень здоровья."""
        self.hp += amount
        print(f"HP увеличено до {self.hp}")

    def upgrade_devil_energy(self, amount: int):
        """Увеличивает запас энергии дьявола."""
        self.devil_energy += amount
        print(f"Энергия дьявола увеличена до {self.devil_energy}")
