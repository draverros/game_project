# adding subclass so that in future each weapon can potentially have
# unique function

# item_type: 
# Weapon
# Armour
# Valuable
# Ring
# Amulet
# Artifact
# Potion


# Weapons

class Weapon:
    def __init__(self, name, damage, item_price, item_type):
        self.name = name
        self.damage = damage
        self.item_price = item_price
        self.item_type = item_type

    def __str__(self):
        return "{} - Damage: +{} - Gold item_price: {} - Type: {} ".format(self.name, self.damage, self.item_price,
                                                                           self.item_type)

class Sword(Weapon):
    def __init__(self, name="Sword", damage=5, item_price=10, item_type="Weapon"):
        Weapon.__init__(self, name, damage, item_price, item_type)
        # Shops: Shining

class Club(Weapon):
    def __init__(self, name="Club", damage=4, item_price=0.1, item_type="Weapon"):
        Weapon.__init__(self, name, damage, item_price, item_type)
        # Shops: Shining

class Crossbow  (Weapon):
    def __init__(self, name="Crossbow", damage=8, item_price=25, item_type="Weapon"):
        Weapon.__init__(self, name, damage, item_price, item_type)

class Dagger(Weapon):
    def __init__(self, name="Dagger", damage=4, item_price=2, item_type="Weapon"):
        Weapon.__init__(self, name, damage, item_price, item_type)
        # Shops: Shining

class Handaxe  (Weapon):
    def __init__(self, name="Handaxe", damage=6, item_price=5, item_type="Weapon"):
        Weapon.__init__(self, name, damage, item_price, item_type)
        # Shops: Shining

class Longbow  (Weapon):
    def __init__(self, name="Longbow", damage=8, item_price=50, item_type="Weapon"):
        Weapon.__init__(self, name, damage, item_price, item_type)

class Longsword  (Weapon):
    def __init__(self, name="Longsword", damage=8, item_price=15, item_type="Weapon"):
        Weapon.__init__(self, name, damage, item_price, item_type)
        # Shops: Shining

class Mace  (Weapon):
    def __init__(self, name="Mace", damage=6, item_price=5, item_type="Weapon"):
        Weapon.__init__(self, name, damage, item_price, item_type)
        # Shops: Shining

class Quarterstaff  (Weapon):
    def __init__(self, name="Quarterstaff", damage=6, item_price=2, item_type="Weapon"):
        Weapon.__init__(self, name, damage, item_price, item_type)
        # Shops: Shining

class Shortbow  (Weapon):
    def __init__(self, name="Shortbow", damage=6, item_price=15, item_type="Weapon"):
        Weapon.__init__(self, name, damage, item_price, item_type)

class Sling  (Weapon):
    def __init__(self, name="Sling", damage=6, item_price=0.1, item_type="Weapon"):
        Weapon.__init__(self, name, damage, item_price, item_type)

class Warhammer  (Weapon):
    def __init__(self, name="Warhammer", damage=8, item_price=15, item_type="Weapon"):
        Weapon.__init__(self, name, damage, item_price, item_type)
        # Shops: Shining

# Armour

class Armour:
    def __init__(self, name, protection, item_price, item_type):
        self.name = name
        self.protection = protection
        self.item_price = item_price
        self.item_type = item_type

    def __str__(self):
        return "{} - Protection: +{} - Gold item_price: {} - Type: {} ".format(self.name, self.protection,
                                                                               self.item_price, self.item_type)

class Cloak(Armour):
    def __init__(self, name="Cloak", protection=6, item_price=5, item_type="Armour"):
        Armour.__init__(self, name, protection, item_price, item_type)

class BreastplateArmour(Armour):
    def __init__(self, name="Breastplate Armour", protection=14, item_price=400, item_type="Armour"):
        Armour.__init__(self, name, protection, item_price, item_type)

class ChainMailArmour(Armour):
    def __init__(self, name="Chain Mail Armour", protection=16, item_price=75, item_type="Armour"):
        Armour.__init__(self, name, protection, item_price, item_type)

class ChainShirtArmour(Armour):
    def __init__(self, name="Chain Mail Armour", protection=13, item_price=50, item_type="Armour"):
        Armour.__init__(self, name, protection, item_price, item_type)

class HalfPlateArmour(Armour):
    def __init__(self, name="Half Plate Armour", protection=15, item_price=750, item_type="Armour"):
        Armour.__init__(self, name, protection, item_price, item_type)

class HideArmour(Armour):
    def __init__(self, name="Hide Armour", protection=12, item_price=10, item_type="Armour"):
        Armour.__init__(self, name, protection, item_price, item_type)

class LeatherArmour(Armour):
    def __init__(self, name="Leather Armour", protection=11, item_price=10, item_type="Armour"):
        Armour.__init__(self, name, protection, item_price, item_type)

class PlateArmour(Armour):
    def __init__(self, name="Plate Armour", protection=18, item_price=1500, item_type="Armour"):
        Armour.__init__(self, name, protection, item_price, item_type)

class RingMailArmour(Armour):
    def __init__(self, name="Ring Mail Armour", protection=14, item_price=30, item_type="Armour"):
        Armour.__init__(self, name, protection, item_price, item_type)

class ScaleMailArmour(Armour):
    def __init__(self, name="Scale Mail Armour", protection=14, item_price=50, item_type="Armour"):
        Armour.__init__(self, name, protection, item_price, item_type)

class PaddedArmour(Armour):
    def __init__(self, name="Padded Armour", protection=11, item_price=5, item_type="Armour"):
        Armour.__init__(self, name, protection, item_price, item_type)

class SplintArmour(Armour):
    def __init__(self, name="Splint Armour", protection=17, item_price=200, item_type="Armour"):
        Armour.__init__(self, name, protection, item_price, item_type)

class StuddedLeatherArmour(Armour):
    def __init__(self, name="Studded Leather Armour", protection=12, item_price=45, item_type="Armour"):
        Armour.__init__(self, name, protection, item_price, item_type)

# Valuable

class Valuable:
    def __init__(self, name, description, item_price, item_type):
        self.name = name
        self.description = description
        self.item_price = item_price
        self.item_type = item_type

    def __str__(self):
        return "{} - Gold item_price: {} - Type: {} ".format(self.name, self.item_price, self.item_type)

# 10 GP Gemstones

class Azurite(Valuable):
    def __init__(self, name="Azurite", description="Opaque mottled deep blue", item_price=10, item_type="Valuable"):
        Valuable.__init__(self, name, description, item_price, item_type)

class BandedAgate(Valuable):
    def __init__(self, name="Banded Agate", description="Translucent striped brown, blue, white, or red", item_price=10,
                 item_type="Valuable"):
        Valuable.__init__(self, name, description, item_price, item_type)

class BlueQuartz(Valuable):
    def __init__(self, name="Blue Quartz", description="Transparent pale blue", item_price=10, item_type="Valuable"):
        Valuable.__init__(self, name, description, item_price, item_type)

class EyeAgate(Valuable):
    def __init__(self, name="Eye Agate", description="Translucent circles of gray, white, brown, blue, or green",
                 item_price=10, item_type="Valuable"):
        Valuable.__init__(self, name, description, item_price, item_type)

class Hematite(Valuable):
    def __init__(self, name="Hematite", description="Opaque gray=black", item_price=10, item_type="Valuable"):
        Valuable.__init__(self, name, description, item_price, item_type)

class LapisLazuli(Valuable):
    def __init__(self, name="Lapis Lazuli", description="Opaque light and dark blue with yellow flecks", item_price=10,
                 item_type="Valuable"):
        Valuable.__init__(self, name, description, item_price, item_type)

class Malachite(Valuable):
    def __init__(self, name="Malachite", description="Opaque striated light and dark green", item_price=10,
                 item_type="Valuable"):
        Valuable.__init__(self, name, description, item_price, item_type)

class MossAgate(Valuable):
    def __init__(self, name="Moss Agate", description="Translucent pink or yellow-white with mossy gray or "
                                                      "green markings", item_price=10, item_type="Valuable"):
        Valuable.__init__(self, name, description, item_price, item_type)

class Obsidian(Valuable):
    def __init__(self, name="Obsidian", description="Opaque black", item_price=10, item_type="Valuable"):
        Valuable.__init__(self, name, description, item_price, item_type)

class Rhodochrosite(Valuable):
    def __init__(self, name="Rhodochrosite", description="Opaque light pink", item_price=10, item_type="Valuable"):
        Valuable.__init__(self, name, description, item_price, item_type)

class TigerEye(Valuable):
    def __init__(self, name="Tiger Eye", description="Translucent brown with golden center", item_price=10,
                 item_type="Valuable"):
        Valuable.__init__(self, name, description, item_price, item_type)

class Turquoise(Valuable):
    def __init__(self, name="Turquoise", description="Opaque light blue-green", item_price=10, item_type="Valuable"):
        Valuable.__init__(self, name, description, item_price, item_type)

# 50 gp Gemstones

class Bloodstone(Valuable):
    def __init__(self, name="Bloodstone", description="Opaque dark gray with red flecks", item_price=50,
                 item_type="Valuable"):
        Valuable.__init__(self, name, description, item_price, item_type)

class Carnelian(Valuable):
    def __init__(self, name="Carnelian", description="Opaque orange to red-brown", item_price=50, item_type="Valuable"):
        Valuable.__init__(self, name, description, item_price, item_type)

class Chalcedony(Valuable):
    def __init__(self, name="Chalcedony", description="Opaque white", item_price=50, item_type="Valuable"):
        Valuable.__init__(self, name, description, item_price, item_type)

class Chrysoprase(Valuable):
    def __init__(self, name="Chrysoprase", description="Translucent green", item_price=50, item_type="Valuable"):
        Valuable.__init__(self, name, description, item_price, item_type)

class Citrine(Valuable):
    def __init__(self, name="Citrine", description="Transparent pale yellow-brown", item_price=50,
                 item_type="Valuable"):
        Valuable.__init__(self, name, description, item_price, item_type)

class Jasper(Valuable):
    def __init__(self, name="Jasper", description="Opaque blue, black, or brown", item_price=50, item_type="Valuable"):
        Valuable.__init__(self, name, description, item_price, item_type)

class Moonstone(Valuable):
    def __init__(self, name="Moonstone", description="Translucent white with pale blue glow", item_price=50,
                 item_type="Valuable"):
        Valuable.__init__(self, name, description, item_price, item_type)

class Onyx(Valuable):
    def __init__(self, name="Onyx", description="Opaque bands of black and white, or pure black or white",
                 item_price=50, item_type="Valuable"):
        Valuable.__init__(self, name, description, item_price, item_type)

class Quartz(Valuable):
    def __init__(self, name="Quartz", description="Transparent white, smoky gray, or yellow", item_price=50,
                 item_type="Valuable"):
        Valuable.__init__(self, name, description, item_price, item_type)

class Sardonyx(Valuable):
    def __init__(self, name="Sardonyx", description="Opaque bands of red and white", item_price=50,
                 item_type="Valuable"):
        Valuable.__init__(self, name, description, item_price, item_type)

class StarRoseQuartz(Valuable):
    def __init__(self, name="Star Rose Quartz", description="Translucent rosy stone with white star-shaped centre",
                 item_price=50, item_type="Valuable"):
        Valuable.__init__(self, name, description, item_price, item_type)

class Zircon(Valuable):
    def __init__(self, name="Zircon", description="Transparent pale blue-green", item_price=50, item_type="Valuable"):
        Valuable.__init__(self, name, description, item_price, item_type)

# 100 gp Gemstones

class Amber(Valuable):
    def __init__(self, name="Amber", description="Transparent watery gold to rich gold", item_price=100,
                 item_type="Valuable"):
        Valuable.__init__(self, name, description, item_price, item_type)

class Amethyst(Valuable):
    def __init__(self, name="Amethyst", description="Transparent deep purple", item_price=100, item_type="Valuable"):
        Valuable.__init__(self, name, description, item_price, item_type)

class Chrysoberyl(Valuable):
    def __init__(self, name="Chrysoberyl", description="Transparent yellow-green to pale green", item_price=100,
                 item_type="Valuable"):
        Valuable.__init__(self, name, description, item_price, item_type)

class Coral(Valuable):
    def __init__(self, name="Coral", description="Opaque crimson", item_price=100, item_type="Valuable"):
        Valuable.__init__(self, name, description, item_price, item_type)

class Garnet(Valuable):
    def __init__(self, name="Garnet", description="Transparent red, brown-green, or violet", item_price=100,
                 item_type="Valuable"):
        Valuable.__init__(self, name, description, item_price, item_type)

class Jade(Valuable):
    def __init__(self, name="Jade", description="Translucent light green, deep green, or white", item_price=100,
                 item_type="Valuable"):
        Valuable.__init__(self, name, description, item_price, item_type)

class Jet(Valuable):
    def __init__(self, name="Jet", description="Opaque deep black", item_price=100, item_type="Valuable"):
        Valuable.__init__(self, name, description, item_price, item_type)

class Pearl(Valuable):
    def __init__(self, name="Pearl", description="Opaque lustrous white, yellow, or pink", item_price=100,
                 item_type="Valuable"):
        Valuable.__init__(self, name, description, item_price, item_type)

class Spinel(Valuable):
    def __init__(self, name="Spinel", description="Transparent red, red-brown, or deep green", item_price=100,
                 item_type="Valuable"):
        Valuable.__init__(self, name, description, item_price, item_type)

class Tourmaline(Valuable):
    def __init__(self, name="Tourmaline", description="Transparent pale green, blue, brown, or red", item_price=100,
                 item_type="Valuable"):
        Valuable.__init__(self, name, description, item_price, item_type)

# 500 gp Gemstones

class Alexandrite(Valuable):
    def __init__(self, name="Alexandrite", description="Transparent dark green", item_price=500, item_type="Valuable"):
        Valuable.__init__(self, name, description, item_price, item_type)

class Aquamarine(Valuable):
    def __init__(self, name="Aquamarine", description="Transparent pale blue-green", item_price=500,
                 item_type="Valuable"):
        Valuable.__init__(self, name, description, item_price, item_type)

class BlackPearl(Valuable):
    def __init__(self, name="Black Pearl", description="Opaque pure black", item_price=500, item_type="Valuable"):
        Valuable.__init__(self, name, description, item_price, item_type)

class BlueSpinel(Valuable):
    def __init__(self, name="Blue Spinel", description="Transparent deep blue", item_price=500, item_type="Valuable"):
        Valuable.__init__(self, name, description, item_price, item_type)

class Peridot(Valuable):
    def __init__(self, name="Peridot", description="Transparent rich olive green", item_price=500,
                 item_type="Valuable"):
        Valuable.__init__(self, name, description, item_price, item_type)

class Topaz(Valuable):
    def __init__(self, name="Topaz", description="Transparent golden yellow", item_price=500, item_type="Valuable"):
        Valuable.__init__(self, name, description, item_price, item_type)

# 1000 gp Gemstones

class BlacOpal(Valuable):
    def __init__(self, name="Black Opal", description="Translucent dark green with black mottling and golden flecks",
                 item_price=1000, item_type="Valuable"):
        Valuable.__init__(self, name, description, item_price, item_type)

class BlueSapphire(Valuable):
    def __init__(self, name="Blue Sapphire", description="Transparent blue-white to medium blue", item_price=1000,
                 item_type="Valuable"):
        Valuable.__init__(self, name, description, item_price, item_type)

class Emerald(Valuable):
    def __init__(self, name="Emerald", description="Transparent deep bright green", item_price=1000,
                 item_type="Valuable"):
        Valuable.__init__(self, name, description, item_price, item_type)

class FireOpal(Valuable):
    def __init__(self, name="Fire Opal", description="Translucent fiery red", item_price=1000, item_type="Valuable"):
        Valuable.__init__(self, name, description, item_price, item_type)

class Opal(Valuable):
    def __init__(self, name="Opal", description="Translucent pale blue with green and golden mottling", item_price=1000,
                 item_type="Valuable"):
        Valuable.__init__(self, name, description, item_price, item_type)

class StarRuby(Valuable):
    def __init__(self, name="Star Ruby", description="Translucent ruby with white star-shaped center", item_price=1000,
                 item_type="Valuable"):
        Valuable.__init__(self, name, description, item_price, item_type)

class StarSapphire(Valuable):
    def __init__(self, name="Star Sapphire", description="Translucent blue sapphire with white star-shaped center",
                 item_price=1000, item_type="Valuable"):
        Valuable.__init__(self, name, description, item_price, item_type)

class YellowSapphire(Valuable):
    def __init__(self, name="Yellow Sapphire", description="Transparent fiery yellow or yellow-green", item_price=1000,
                 item_type="Valuable"):
        Valuable.__init__(self, name, description, item_price, item_type)

# 5000 gp Gemstones

class BlackSapphire(Valuable):
    def __init__(self, name="Black Sapphire", description="Translucent lustrous black with glowing highlights",
                 item_price=5000, item_type="Valuable"):
        Valuable.__init__(self, name, description, item_price, item_type)

class Diamond(Valuable):
    def __init__(self, name="Diamond", description="Transparent blue-white, canary, pink, brown, or blue",
                 item_price=5000, item_type="Valuable"):
        Valuable.__init__(self, name, description, item_price, item_type)

class Jacinth(Valuable):
    def __init__(self, name="Jacinth", description="Transparent fiery orange", item_price=5000, item_type="Valuable"):
        Valuable.__init__(self, name, description, item_price, item_type)

class Ruby(Valuable):
    def __init__(self, name="Ruby", description="Transparent clear red to deep crimson", item_price=5000,
                 item_type="Valuable"):
        Valuable.__init__(self, name, description, item_price, item_type)

# Rings

class Ring:
    def __init__(self, name, description, item_price, item_type):
        self.name = name
        self.description = description
        self.item_price = item_price
        self.item_type = item_type

    def __str__(self):
        return "{} - {} - Gold item_price: {} - Type: {} ".format(self.name, self.description, self.item_price,
                                                                  self.item_type)

class WeakRingStr(Ring):
    def __init__(self, name="Weak Ring of Strength", description="You gain a +1 bonus to your strength while wearing "
                                                                 "this ring.", item_price=100, item_type="Ring"):
        Ring.__init__(self, name, description, item_price, item_type)

class WeakRingDex(Ring):
    def __init__(self, name="Weak Ring of Dexterity", description="You gain a +1 bonus to your dexterity while wearing "
                                                                  "this ring.", item_price=100, item_type="Ring"):
        Ring.__init__(self, name, description, item_price, item_type)

class WeakRingInt(Ring):
    def __init__(self, name="Weak Ring of Intelligence", description="You gain a +1 bonus to your intelligence while "
                                                                     "wearing this ring.", item_price=100,
                 item_type="Ring"):
        Ring.__init__(self, name, description, item_price, item_type)

class WeakRingCon(Ring):
    def __init__(self, name="Weak Ring of Constitution", description="You gain a +1 bonus to your constitution while "
                                                                     "wearing this ring.", item_price=100,
                 item_type="Ring"):
        Ring.__init__(self, name, description, item_price, item_type)

class WeakRingCha(Ring):
    def __init__(self, name="Weak Ring of Charisma", description="You gain a +2 bonus to your charisma while wearing "
                                                                 "this ring.", item_price=100, item_type="Ring"):
        Ring.__init__(self, name, description, item_price, item_type)


class RingProt(Ring):
    def __init__(self, name="Ring of Protection", description="You gain a +1 bonus to AC while wearing this ring.",
                 item_price=200, item_type="Ring"):
        Ring.__init__(self, name, description, item_price, item_type)

class RingLife(Ring):
    def __init__(self, name="Ring of Life", description="You gain a 10 bonus to health while wearing this ring.",
                 item_price=200, item_type="Ring"):
        Ring.__init__(self, name, description, item_price, item_type)

class RingStr(Ring):
    def __init__(self, name="Ring of Strength", description="You gain a +2 bonus to your strength while wearing "
                                                            "this ring.", item_price=200, item_type="Ring"):
        Ring.__init__(self, name, description, item_price, item_type)

class RingDex(Ring):
    def __init__(self, name="Ring of Dexterity", description="You gain a +2 bonus to your dexterity while wearing "
                                                             "this ring.", item_price=200, item_type="Ring"):
        Ring.__init__(self, name, description, item_price, item_type)

class RingInt(Ring):
    def __init__(self, name="Ring of Intelligence", description="You gain a +2 bonus to your intelligence while wearing"
                                                                " this ring.", item_price=200, item_type="Ring"):
        Ring.__init__(self, name, description, item_price, item_type)

class RingCon(Ring):
    def __init__(self, name="Ring of Constitution", description="You gain a +2 bonus to your constitution while wearing"
                                                                "this ring.", item_price=200, item_type="Ring"):
        Ring.__init__(self, name, description, item_price, item_type)

class RingCha(Ring):
    def __init__(self, name="Ring of Charisma", description="You gain a +2 bonus to your charisma while wearing "
                                                            "this ring.", item_price=200, item_type="Ring"):
        Ring.__init__(self, name, description, item_price, item_type)


# Amulets

class Amulet:
    def __init__(self, name, description, item_price, item_type):
        self.name = name
        self.description = description
        self.item_price = item_price
        self.item_type = item_type

    def __str__(self):
        return "{} - {} - Gold item_price: {} - Type: {} ".format(self.name, self.description, self.item_price,
                                                                  self.item_type)

class WeakAmuletStr(Amulet):
    def __init__(self, name="Weak Amulet of Strength", description="You gain a +1 bonus to your strength while wearing "
                                                                   "this amulet.", item_price=100, item_type="Amulet"):
        Amulet.__init__(self, name, description, item_price, item_type)

class WeakAmuletDex(Amulet):
    def __init__(self, name="Weak Amulet of Dexterity", description="You gain a +1 bonus to your dexterity while "
                                                                    "wearing this amulet.", item_price=100,
                 item_type="Amulet"):
        Amulet.__init__(self, name, description, item_price, item_type)

class WeakAmuletInt(Amulet):
    def __init__(self, name="Weak Amulet of Intelligence", description="You gain a +1 bonus to your intelligence while "
                                                                       "wearing this amulet.", item_price=100,
                 item_type="Amulet"):
        Amulet.__init__(self, name, description, item_price, item_type)

class WeakAmuletCon(Amulet):
    def __init__(self, name="Weak Amulet of Constitution", description="You gain a +1 bonus to your constitution while "
                                                                       "wearing this amulet.", item_price=100,
                 item_type="Amulet"):
        Amulet.__init__(self, name, description, item_price, item_type)

class WeakAmuletCha(Amulet):
    def __init__(self, name="Weak Amulet of Charisma", description="You gain a +1 bonus to your charisma while wearing "
                                                                   "this amulet.", item_price=100, item_type="Amulet"):
        Amulet.__init__(self, name, description, item_price, item_type)

class AmuletProt(Amulet):
    def __init__(self, name="Amulet of Protection", description="You gain a +1 bonus to AC while wearing this amulet.",
                 item_price=200, item_type="Amulet"):
        Amulet.__init__(self, name, description, item_price, item_type)

class AmuletLife(Amulet):
    def __init__(self, name="Amulet of Life", description="You gain a 10 bonus to health while wearing this amulet.",
                 item_price=200, item_type="Amulet"):
        Amulet.__init__(self, name, description, item_price, item_type)

class AmuletStr(Amulet):
    def __init__(self, name="Amulet of Strength", description="You gain a +2 bonus to your strength while wearing "
                                                              "this amulet.", item_price=200, item_type="Amulet"):
        Amulet.__init__(self, name, description, item_price, item_type)

class AmuletDex(Amulet):
    def __init__(self, name="Amulet of Dexterity", description="You gain a +2 bonus to your dexterity while wearing "
                                                               "this amulet.", item_price=200, item_type="Amulet"):
        Amulet.__init__(self, name, description, item_price, item_type)

class AmuletInt(Amulet):
    def __init__(self, name="Amulet of Intelligence", description="You gain a +2 bonus to your intelligence while "
                                                                  "wearing this amulet.", item_price=200,
                 item_type="Amulet"):
        Amulet.__init__(self, name, description, item_price, item_type)

class AmuletCon(Amulet):
    def __init__(self, name="Amulet of Constitution", description="You gain a +2 bonus to your constitution while "
                                                                  "wearing this amulet.", item_price=200,
                 item_type="Amulet"):
        Amulet.__init__(self, name, description, item_price, item_type)

class AmuletCha(Amulet):
    def __init__(self, name="Amulet of Charisma", description="You gain a +2 bonus to your charisma while wearing "
                                                              "this amulet.", item_price=200, item_type="Amulet"):
        Amulet.__init__(self, name, description, item_price, item_type)

# Artifacts

class Artifact:
    def __init__(self, name, description, item_price, item_type):
        self.name = name
        self.description = description
        self.item_price = item_price
        self.item_type = item_type

    def __str__(self):
        return "{} - {} - Gold item_price: {} - Type: {} ".format(self.name, self.description, self.item_price,
                                                                  self.item_type)

# Potions

class Potion:
    def __init__(self, name, description, heal, item_price, item_type):
        self.name = name
        self.description = description
        self.heal = heal
        self.item_price = item_price
        self.item_type = item_type

    def __str__(self):
        return "{} - {} - Gold item_price: {} - Type: {} ".format(self.name, self.description, self.heal,
                                                                  self.item_price, self.item_type)

class HealPotCommon(Potion):
    def __init__(self, name="Healing Potion", description="This healing potion restores 10HP", heal=10, item_price=50,
                 item_type="Potion"):
        Potion.__init__(self, name, description, heal, Valuable, item_type)

class HealPotGreater(Potion):
    def __init__(self, name="Greater Healing Potion", description="This healing potion restores 20HP", heal=20,
                 item_price=200, item_type="Potion"):
        Potion.__init__(self, name, description, heal, Valuable, item_type)

class HealPotSuperior(Potion):
    def __init__(self, name="Superior Healing Potion", description="This healing potion restores 40HP", heal=40,
                 item_price=750, item_type="Potion"):
        Potion.__init__(self, name, description, heal, Valuable, item_type)


class HealPotSupreme(Potion):
    def __init__(self, name="Supreme Healing Potion", description="This healing potion restores 60HP", heal=60,
                 item_price=3500, item_type="Potion"):
        Potion.__init__(self, name, description, heal, Valuable, item_type)



















