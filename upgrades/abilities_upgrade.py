class UpgradeTree:
    def __init__(self):
        self.unlocked = []

    def unlock_ability(self, ability, cost, currency_system):
        if currency_system.spend_orbs(cost):
            self.unlocked.append(ability)
            print(f"Способность '{ability}' разблокирована.")
        else:
            print(f"Не удалось разблокировать '{ability}'.")

    def show_upgrades(self):
        print("Разблокированные умения:", self.unlocked)