from items import*

class Player(object):
    def __init__(self):
        self.name = ""
        self.race = ""
        self.profession = ""
        self.guild = ""
        self.equipped_weapon = Club()
        self.equipped_armour = HideArmour()
        self.equipped_ring = RingStr()
        self.equipped_amulet = AmuletStr()
        # self.equipped_artifact = ""
        self.inventory = [BreastplateArmour(), Longsword(), Aquamarine(), Club(), Azurite(), RingProt(), AmuletProt(),
                          PaddedArmour()]
        self.gold = 1000
        self.location = ""
        self.sell_mod = 0
        self.buy_mod = 0

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
        self.charisma_profession = 0
        self.hp_profession = 0
        self.mp_profession = 0

        # Modifiers
        self.constitution_mod = 0
        self.damage_mod = 0
        self.armour_class = 0

        # Player final
        self.strength = 0
        self.dexterity = 0
        self.intelligence = 0
        self.constitution = 0
        self.charisma = 0
        self.max_hp = 0
        self.current_hp = 0
        self.max_mp = 0
        self.current_mp = 0

        self.game_over = False

        