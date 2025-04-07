class PlayerStats:
    def __init__(self):
        self.hp = 100
        self.devil_energy = 50

    def upgrade_hp(self, amount):
        self.hp += amount
        print(f"HP увеличено до {self.hp}")

    def upgrade_devil_energy(self, amount):
        self.devil_energy += amount
        print(f"Энергия дьявола увеличена до {self.devil_energy}")