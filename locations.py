from items import*
from player import Player
import lists


def list_to_text(my_list):
    combined_text = "\n"
    for i in range(len(my_list)):
        combined_text += str(i) + ") " + my_list[i] + "\n"
    return combined_text + "\n"

def check_menu_range(question, list_name, is_cancelable=False):
    index = int(input(question + list_to_text(list_name)))
    while True:
        if is_cancelable and index == -1:
            return index
        elif index < 0 or index > len(list_name) - 1:
            index = int(input("Invalid choice please try again\n"))
        else:
            return index

def show_inventory(inventory_list):
    if len(inventory_list) < 1:
        print("Inventory is empty.")
        return
    uniq_inventory_list = list(set(inventory_list))
    for i in range(len(uniq_inventory_list)):
        print(
            str(i) + ") " + str(uniq_inventory_list[i]) + "(" + str(inventory_list.count(uniq_inventory_list[i]))
            + ")")


# Neverwinter

# Shining Knight Arms and Armour

def ShiningKnight(Player):
	print(f"You currently have {Player.gold} gold.")
	shop_choice = check_menu_range("Welcome, traveller, to the Shining Knight Arms and Armour, "
	                              "the finest weapons and amour in the whole Neverwinter! Are you buying "
	                              "or selling?", ["Buy", "Sell", "Exit"], True)
	if shop_choice == -1:
	    print("error")

	elif shop_choice == 0:
	     print("What would you like to buy? ")
	 #    print("0) Club - Damage: 4 - Cost: 0.1 gold")
	 #    print("1) Dagger - Damage: 4 - Cost: 2 gold")
	 #    print("2) Handaxe - Damage: 6 - Cost: 5 gold")
	 #    print("3) Longsword - Damage: 8 - Cost: 15 gold")
	 #    print("4) Mace - Damage: 6 - Cost: 5 ")
	 #    print("5) Quarterstaff - Damage: 6 - Cost: 2")
	 #    print("6) Warhammer - Damage: 8 - Cost: 15")
	 #    print("7) Brestplate Armour - Protection: 14 - Cost: 400")
	 #    choice = input("Choice: ")
		
		# if choice == ("0"):

		# 	if Player.gold < 0.1:
		# 		print("You can't afford it.")
		# 	else:
		# 	    Player.inventory.append(Club())
		# 	    Player.gold -= 0.1
		# 	    print("You got a Club")
		# 	    print("")

		# elif choice == ("1"):
		# 	if Player.gold < 2:
		# 		print("You can't afford it.")
		# 	else:
		# 		Player.inventory.append(Dagger())
		# 		Player.gold -= 2
		# 		print("You got a Dagger")
		# 		print("")

		# elif choice == ("2"):
		# 	if Player.gold < 5:
		# 		print("You can't afford it.")
		# 	else:
		# 		Player.inventory.append(Handaxe())
		# 		Player.gold -= 5
		# 		print("You got a Handaxe.")
		# 		print("")

		# elif choice == ("3"):
		# 	if Player.gold < 15:
		# 		print("You can't afford it.")
		# 	else:
		# 		Player.inventory.append(Longsword())
		# 		Player.gold -= 15
		# 		print("You got a Longsword.")
		# 		print("")

		# elif choice == ("4"):
		# 	if Player.gold < 5:
		# 		print("You can't afford it.")
		# 	else:
		# 		Player.inventory.append(Mace())
		# 		Player.gold -= 5
		# 		print("You got a Mace.")
		# 		print("")

		# elif choice == ("5"):
		# 	if Player.gold < 2:
		# 		print("You can't afford it.")
		# 	else:
		# 		Player.inventory.append(Quarterstaff())
		# 		Player.gold -= 2
		# 		print("You got a Quarterstaff.")
		# 		print("")

		# elif choice == ("6"):
		# 	if Player.gold < 15:
		# 		print("You can't afford it.")
		# 	else:
		# 		Player.inventory.append(Warhammer())
		# 		Player.gold -= 15
		# 		print("You got a Warhammer.")
		# 		print("")

		# elif choice == ("7"):
		# 	if Player.gold < 400:
		# 		print("You can't afford it.")
		# 	else:
		# 		Player.inventory.append(BrestplateArmour())
		# 		Player.gold -= 400
		# 		print("You got a Brestplate Armour")
		# 		print("")

	elif shop_choice == 1:
		if len(Player.inventory) > 0:
			print("What would you like to sell? A weapon(W), an armour(A) or other(O)?")
			sell_choice = input("Choice: ").upper()

			if sell_choice == "W":
				Weapons = [item for item in Player.inventory if isinstance(item, Weapon)]
				for i,item in enumerate(Weapons,1):
					print("{}.{}".format(i,item))
					weapon_sell_choice = input("Choice: ")
					Player.inventory.remove(Weapons[int(weapon_sell_choice)-1])
					sell_val = item.value * Player.sell_mod
					Player.gold += sell_val
					print(Player.gold)

			elif sell_choice == "A":
				Armours = [item for item in Player.inventory if isinstance(item, Armour)]
				for i,item in enumerate(Armours,1):
					print("{}.{}".format(i,item))
					armour_sell_choice = input("Choice: ")
					Player.inventory.remove(Armours[int(armour_sell_choice)-1])
					sell_val = item.value * Player.sell_mod
					Player.gold += sell_val
					print(Player.gold)

			elif sell_choice == "O":
				print("Would you like to sell a ring(R), amulet(A) or valuable(V)")
				other_sell_choice = input("Choice: ").upper()

				if other_sell_choice == "R":
					Rings = [item for item in Player.inventory if isinstance(item, Ring)]
					for i,item in enumerate(Rings,1):
						print("{}.{}".format(i,item))
						ring_sell_choice = input("Choice: ")
						Player.inventory.remove(Rings[int(ring_sell_choice)-1])
						sell_val = item.value * Player.sell_mod
						Player.gold += sell_val
						print(Player.gold)

				elif other_sell_choice == "A":
					Amulets = [item for item in Player.inventory if isinstance(item, Amulet)]
					for i,item in enumerate(Amulets,1):
						print("{}.{}".format(i,item))
						amulet_sell_choice = input("Choice: ")
						Player.inventory.remove(Amulets[int(amulet_sell_choice)-1])
						sell_val = item.value * Player.sell_mod
						Player.gold += sell_val
						print(Player.gold)

				elif other_sell_choice == "V":
					Valuables = [item for item in Player.inventory if isinstance(item, Valuable)]
					for i,item in enumerate(Valuables,1):
						print("{}.{}".format(i,item))
						valuable_sell_choice = input("Choice: ")
						Player.inventory.remove(Valuables[int(valuable_sell_choice)-1])
						sell_val = item.value * Player.sell_mod
						Player.gold += sell_val
						print(Player.gold)

	elif shop_choice == 2:
		print("")

# Tarmalune Trade House - shop with everything except weapons
def Tarmalune(Player):
	print("Tarmalune Trade House")

# House of Knowledge - Temple to heal wounds for money
def HouseOfKnowledge(Player):
	print("House of Knowledge") 

# Shining Serpent Inn - Inn with drinks and a bed to rest
def ShiningSerpent(Player):
	print("Shining Serpent Inn")

# House of a Thousand Faces - Headquarters of the Harpers
def HouseOfFaces(Player):
	print("House of a Thousand Faces")

# Dannar's Mechanical Marvels - artifacts shop
def DannarsMechanical(Player):
	print("Dannar's Mechanical Marvels")

# Maskado's Maps and Legends - shop selling rumors, maps and legends
def MaskadosMaps(Player):
	print("Maskado's Maps and Legends")

# Cloak Tower - Wizard tower
def CloakTower(Player):
	print("Cloak Tower")