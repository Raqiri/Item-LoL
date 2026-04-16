class itemDefault:
    def __init__(self):
        self.name = ""
        self.effect = ""
        self.effectValue = 0
        self.description = ""
    def useItem(self, player):
        pass

# 1. Infinity Edge
class infinityEdge(itemDefault):
    def __init__(self):
        super().__init__()
        self.name = "Infinity Edge"
        self.effect = "critical strike damage"
        self.effectValue = 40
        self.description = "Boost critical strike damage massively"
    def useItem(self, player):
        print(f"{player} used {self.name}, critical strike damage increased by {self.effectValue}%")

# 2. Zhonya's Hourglass
class zhonyasHourglass(itemDefault):
    def __init__(self):
        super().__init__()
        self.name = "Zhonya's Hourglass"
        self.effect = "stasis"
        self.effectValue = 2
        self.description = "Enter stasis and become invulnerable briefly"
    def useItem(self, player):
        print(f"{player} used {self.name}, entered stasis for {self.effectValue} seconds")

# 3. Banshee's Veil
class bansheesVeil(itemDefault):
    def __init__(self):
        super().__init__()
        self.name = "Banshee's Veil"
        self.effect = "spell shield"
        self.effectValue = 1
        self.description = "Block the next incoming enemy spell"
    def useItem(self, player):
        print(f"{player} used {self.name}, blocked {self.effectValue} incoming spell")

# 4. Rabadon's Deathcap
class rabadonsDeathcap(itemDefault):
    def __init__(self):
        super().__init__()
        self.name = "Rabadon's Deathcap"
        self.effect = "ability power"
        self.effectValue = 35
        self.description = "Amplify total ability power by a large percentage"
    def useItem(self, player):
        print(f"{player} used {self.name}, total ability power amplified by {self.effectValue}%")

# 5. Warmog's Armor
class warmogsArmor(itemDefault):
    def __init__(self):
        super().__init__()
        self.name = "Warmog's Armor"
        self.effect = "health regeneration"
        self.effectValue = 200
        self.description = "Rapidly regenerate health out of combat"
    def useItem(self, player):
        print(f"{player} used {self.name}, regenerating {self.effectValue} HP per second")
