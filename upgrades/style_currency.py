class CurrencySystem:
    def __init__(self):
        self.red_orbs = 0
        self.style_points = 0

    def add_orbs(self, amount):
        self.red_orbs += amount
        print(f"+{amount} красных сфер")

    def add_style_points(self, amount):
        self.style_points += amount
        print(f"+{amount} очков стиля")

    def spend_orbs(self, cost):
        if self.red_orbs >= cost:
            self.red_orbs -= cost
            return True
        else:
            print("Недостаточно сфер.")
            return False