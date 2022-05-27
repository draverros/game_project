import items

class Player:
    def __init__(self):
        self.name = ""
        self.race = ""
        self.profession = ""
        self.inventory = [items.Club(), items.BrestplateArmour()]
        self.gold = 1
        self.location = ""

        # Roll Stats
        self.strength_roll = 0
        self.dexterity_roll = 0
        self.intelligence_roll = 0
        self.constitution_roll = 0
        self.charisma_roll = 0

        # Race Stats
        self.strength_race = 0
        self.dexterity_race = 0
        self.intelligence_race = 0
        self.constitution_race = 0
        self.charisma_race = 0
        self.hp_race = 0

        # Class Stats
        self.strength_profession = 0
        self.dexterity_profession = 0
        self.intelligence_profession = 0
        self.constitution_profession = 0
        self.charsma_profession = 0
        self.hp_profession = 0
        self.mp_profession = 0

        # Modifiers
        self.constitution_mod = 0

        # Player final
        self.strength = 0
        self.dexterity = 0
        self.intelligence = 0
        self.constitution = 0
        self.charisma = 0
        self.hp = 0
        self.mp = 0

        self.game_over = False

        