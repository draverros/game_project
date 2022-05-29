

# adding subclass so that in future each weapon can potentialy have
# unique function

# List: 
# Weapons
# Armour
# Valuables (Gems and Art)



# Weapons

class Weapon:
    def __init__(self, name, damage, value):
        self.name = name
        self.damage = damage
        self.value = value
        
    def __str__(self):
        return "{} +{} damage ".format(self.name, self.damage)

class Club(Weapon):
    def __init__(self, name="Club", damage=4, value=0.1):
        Weapon.__init__(self, name, damage, value)

class Crossbow  (Weapon):
    def __init__(self, name="Crossbow", damage=8, value=25):
        Weapon.__init__(self, name, damage, value)

class Dagger(Weapon):
    def __init__(self, name="Dagger", damage=4, value=2):
        Weapon.__init__(self, name, damage, value)

class Handaxe  (Weapon):
    def __init__(self, name="Handaxe", damage=6, value=5):
        Weapon.__init__(self, name, damage, value)

class Longbow  (Weapon):
    def __init__(self, name="Longbow", damage=8, value=50):
        Weapon.__init__(self, name, damage, value)

class Longsword  (Weapon):
    def __init__(self, name="Longsword", damage=8, value=15):
        Weapon.__init__(self, name, damage, value)

class Mace  (Weapon):
    def __init__(self, name="Mace", damage=6, value=5):
        Weapon.__init__(self, name, damage, value)

class Quarterstaff  (Weapon):
    def __init__(self, name="Quarterstaff", damage=6, value=2):
        Weapon.__init__(self, name, damage, value)

class Shortbow  (Weapon):
    def __init__(self, name="Shortbow", damage=6, value=15):
        Weapon.__init__(self, name, damage, value)

class Sling  (Weapon):
    def __init__(self, name="Sling", damage=6, value=0.1):
        Weapon.__init__(self, name, damage, value)

class Warhammer  (Weapon):
    def __init__(self, name="Warhammer", damage=8, value=15):
        Weapon.__init__(self, name, damage, value)

# Armour

class Armour:
    def __init__(self, name, protection, value):
        self.name = name
        self.protection = protection
        self.value = value
        
    def __str__(self):
        return "{} +{} protection ".format(self.name, self.protection)

class BrestplateArmour(Armour):
    def __init__(self, name="Brestplate Armour", protection=14, value=400):
        Armour.__init__(self, name, protection, value)

class ChainMailArmour(Armour):
    def __init__(self, name="Chain Mail Armour", protection=16, value=75):
        Armour.__init__(self, name, protection, value)

class ChainShirtArmour(Armour):
    def __init__(self, name="Chain Mail Armour", protection=13, value=50):
        Armour.__init__(self, name, protection, value)

class HalfPlateArmour(Armour):
    def __init__(self, name="Half Plate Armour", protection=15, value=750):
        Armour.__init__(self, name, protection, value)

class HideArmour(Armour):
    def __init__(self, name="Hide Armour", protection=12, value=10):
        Armour.__init__(self, name, protection, value)

class LeatherArmour(Armour):
    def __init__(self, name="Leather Armour", protection=11, value=10):
        Armour.__init__(self, name, protection, value)

class PlateArmour(Armour):
    def __init__(self, name="Plate Armour", protection=18, value=1500):
        Armour.__init__(self, name, protection, value)

class RingMailArmour(Armour):
    def __init__(self, name="Ring Mail Armour", protection=14, value=30):
        Armour.__init__(self, name, protection, value)

class ScaleMailArmour(Armour):
    def __init__(self, name="Scale Mail Armour", protection=14, value=50):
        Armour.__init__(self, name, protection, value)

class PaddedArmour(Armour):
    def __init__(self, name="Padded Armour", protection=11, value=5):
        Armour.__init__(self, name, protection, value)

class SplintArmour(Armour):
    def __init__(self, name="Splint Armour", protection=17, value=200):
        Armour.__init__(self, name, protection, value)

class StuddedLeatherArmour(Armour):
    def __init__(self, name="Studded Leather Armour", protection=12, value=45):
        Armour.__init__(self, name, protection, value)

# Valuable

class Valuable:
    def __init__(self, name, value):
        self.name = name
        self.description = description
        self.value = value

# 10 GP Gemstones

class Azurite(Valuable):
    def __init__(self, name="Azurite", description="Opaque mottled deep blue", value=10):
        Valuable.__init__(self, name, description, value)

class BandedAgate(Valuable):
    def __init__(self, name="Banded Agate", description="Translucent striped brown, blue, white, or red", value=10):
        Valuable.__init__(self, name, description, value)

class BlueQuartz(Valuable):
    def __init__(self, name="Blue Quartz", description="Transparent pale blue", value=10):
        Valuable.__init__(self, name, description, value)

class EyeAgate(Valuable):
    def __init__(self, name="Eye Agate", description="Translucent circles of gray, white, brown, blue, or green", value=10):
        Valuable.__init__(self, name, description, value)

class Hematite(Valuable):
    def __init__(self, name="Hematite", description="Opaque gray=black", value=10):
        Valuable.__init__(self, name, description, value)

class LapisLazuli(Valuable):
    def __init__(self, name="Lapis Lazuli", description="Opaque light and dark blue with yellow flecks", value=10):
        Valuable.__init__(self, name, description, value)

class Malachite(Valuable):
    def __init__(self, name="Malachite", description="Opaque striated light and dark green", value=10):
        Valuable.__init__(self, name, description, value)

class MossAgate(Valuable):
    def __init__(self, name="Moss Agate", description="Translucent pink or yellow-white with mossy gray or green markings", value=10):
        Valuable.__init__(self, name, description, value)

class Obsidian(Valuable):
    def __init__(self, name="Obsidian", description="Opaque black", value=10):
        Valuable.__init__(self, name, description, value)

class Rhodochrosite(Valuable):
    def __init__(self, name="Rhodochrosite", description="Opaque light pink", value=10):
        Valuable.__init__(self, name, description, value)

class TigerEye(Valuable):
    def __init__(self, name="Tiger Eye", description="Translucent brown with golden center", value=10):
        Valuable.__init__(self, name, description, value)

class Turquoise(Valuable):
    def __init__(self, name="Turquoise", description="Opaque light blue-green", value=10):
        Valuable.__init__(self, name, description, value)

# 50 gp Gemstones

class Bloodstone(Valuable):
    def __init__(self, name="Bloodstone", description="Opaque dark gray with red flecks", value=50):
        Valuable.__init__(self, name, description, value)

class Carnelian(Valuable):
    def __init__(self, name="Carnelian", description="Opaque orange to red-brown", value=50):
        Valuable.__init__(self, name, description, value)

class Chalcedony(Valuable):
    def __init__(self, name="Chalcedony", description="Opaque white", value=50):
        Valuable.__init__(self, name, description, value)

class Chrysoprase(Valuable):
    def __init__(self, name="Chrysoprase", description="Translucent green", value=50):
        Valuable.__init__(self, name, description, value)

class Citrine(Valuable):
    def __init__(self, name="Citrine", description="Transparent pale yellow-brown", value=50):
        Valuable.__init__(self, name, description, value)

class Jasper(Valuable):
    def __init__(self, name="Jasper", description="Opaque blue, black, or brown", value=50):
        Valuable.__init__(self, name, description, value)

class Moonstone(Valuable):
    def __init__(self, name="Moonstone", description="Translucent white with pale blue glow", value=50):
        Valuable.__init__(self, name, description, value)

class Onyx(Valuable):
    def __init__(self, name="Onyx", description="Opaque bands of black and white, or pure black or white", value=50):
        Valuable.__init__(self, name, description, value)

class Quartz(Valuable):
    def __init__(self, name="Quartz", description="Transparent white, smoky gray, or yellow", value=50):
        Valuable.__init__(self, name, description, value)

class Sardonyx(Valuable):
    def __init__(self, name="Sardonyx", description="Opaque bands of red and white", value=50):
        Valuable.__init__(self, name, description, value)

class StarRoseQuartz(Valuable):
    def __init__(self, name="Star Rose Quartz", description="Translucent rosy stone with white star-shaped centre", value=50):
        Valuable.__init__(self, name, description, value)

class Zircon(Valuable):
    def __init__(self, name="Zircon", description="Transparent pale blue-green", value=50):
        Valuable.__init__(self, name, description, value)

# 100 gp Gemstones

class Amber(Valuable):
    def __init__(self, name="Amber", description="Transparent watery gold to rich gold", value=100):
        Valuable.__init__(self, name, description, value)

class Amethyst(Valuable):
    def __init__(self, name="Amethyst", description="Transparent deep purple", value=100):
        Valuable.__init__(self, name, description, value)

class Chrysoberyl(Valuable):
    def __init__(self, name="Chrysoberyl", description="Transparent yellow-green to pale green", value=100):
        Valuable.__init__(self, name, description, value)

class Coral(Valuable):
    def __init__(self, name="Coral", description="Opaque crimson", value=100):
        Valuable.__init__(self, name, description, value)

class Garnet(Valuable):
    def __init__(self, name="Garnet", description="Transparent red, brown-green, or violet", value=100):
        Valuable.__init__(self, name, description, value)

class Jade(Valuable):
    def __init__(self, name="Jade", description="Translucent light green, deep green, or white", value=100):
        Valuable.__init__(self, name, description, value)

class Jet(Valuable):
    def __init__(self, name="Jet", description="Opaque deep black", value=100):
        Valuable.__init__(self, name, description, value)

class Pearl(Valuable):
    def __init__(self, name="Pearl", description="Opaque lustrous white, yellow, or pink", value=100):
        Valuable.__init__(self, name, description, value)

class Spinel(Valuable):
    def __init__(self, name="Spinel", description="Transparent red, red-brown, or deep green", value=100):
        Valuable.__init__(self, name, description, value)

class Tourmaline(Valuable):
    def __init__(self, name="Tourmaline", description="Transparent pale green, blue, brown, or red", value=100):
        Valuable.__init__(self, name, description, value)

# 500 gp Gemstones

class Alexandrite(Valuable):
    def __init__(self, name="Alexandrite", description="Transparent dark green", value=500):
        Valuable.__init__(self, name, description, value)

class Aquamarine(Valuable):
    def __init__(self, name="Aquamarine", description="Transparent pale blue-green", value=500):
        Valuable.__init__(self, name, description, value)

class BlackPearl(Valuable):
    def __init__(self, name="Black Pearl", description="Opaque pure black", value=500):
        Valuable.__init__(self, name, description, value)

class BlueSpinel(Valuable):
    def __init__(self, name="Blue Spinel", description="Transparent deep blue", value=500):
        Valuable.__init__(self, name, description, value)

class Peridot(Valuable):
    def __init__(self, name="Peridot", description="Transparent rich olive green", value=500):
        Valuable.__init__(self, name, description, value)

class Topaz(Valuable):
    def __init__(self, name="Topaz", description="Transparent golden yellow", value=500):
        Valuable.__init__(self, name, description, value)

# 1000 gp Gemstones

class BlacOpal(Valuable):
    def __init__(self, name="Black Opal", description="Translucent dark green with black mottling and golden flecks", value=1000):
        Valuable.__init__(self, name, description, value)

class BlueSapphire(Valuable):
    def __init__(self, name="Blue Sapphire", description="Transparent blue-white to medium blue", value=1000):
        Valuable.__init__(self, name, description, value)

class Emerald(Valuable):
    def __init__(self, name="Emerald", description="Transparent deep bright green", value=1000):
        Valuable.__init__(self, name, description, value)

class FireOpal(Valuable):
    def __init__(self, name="Fire Opal", description="Translucent fiery red", value=1000):
        Valuable.__init__(self, name, description, value)

class Opal(Valuable):
    def __init__(self, name="Opal", description="Translucent pale blue with green and golden mottling", value=1000):
        Valuable.__init__(self, name, description, value)

class StarRuby(Valuable):
    def __init__(self, name="Star Ruby", description="Translucent ruby with white star-shaped center", value=1000):
        Valuable.__init__(self, name, description, value)

class StarSapphire(Valuable):
    def __init__(self, name="Star Sapphire", description="Translucent blue sapphire with white star-shaped center", value=1000):
        Valuable.__init__(self, name, description, value)

class YellowSapphire(Valuable):
    def __init__(self, name="Yellow Sapphire", description="Transparent fiery yellow or yellow-green", value=1000):
        Valuable.__init__(self, name, description, value)

# 5000 gp Gemstones

class BlackSapphire(Valuable):
    def __init__(self, name="Black Sapphire", description="Translucent lustrous black with glowing highlights", value=5000):
        Valuable.__init__(self, name, description, value)

class Diamond(Valuable):
    def __init__(self, name="Diamond", description="Transparent blue-white, canary, pink, brown, or blue", value=5000):
        Valuable.__init__(self, name, description, value)

class Jacinth(Valuable):
    def __init__(self, name="Jacinth", description="Transparent fiery orange", value=5000):
        Valuable.__init__(self, name, description, value)

class Ruby(Valuable):
    def __init__(self, name="Ruby", description="Transparent clear red to deep crimson", value=5000):
        Valuable.__init__(self, name, description, value)































