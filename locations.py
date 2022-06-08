from items import*
from player import Player

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
	while not Player.game_over:
		print("")
		print(f"You currently have {Player.gold} gold.")
		print("")

		ShiningSellListWeapons = [Club(), Sword(), Dagger(), Handaxe(), Longsword(), Mace(), Quarterstaff(), Warhammer()]
		ShiningSellListArmours = [Cloak(), BrestplateArmour(), ChainMailArmour(), ChainShirtArmour(), HalfPlateArmour(), HideArmour(), LeatherArmour(), PlateArmour(), RingMailArmour(), ScaleMailArmour(), PaddedArmour(), SplintArmour(), StuddedLeatherArmour()]

		shop_choice = check_menu_range("Welcome, traveller, to the Shining Knight Arms and Armour, "
		                              "the finest weapons and amour in the whole Neverwinter! Are you buying "
		                              "or selling?", ["Buy", "Sell", "Exit"], True)

		if shop_choice == -1:
		    print("error")

		if shop_choice == 0:
		    print("What would you like to buy, Weapon(W) or Armour(A). Exit (E)")
		    buy_shop_choice = input("Choice: ").upper()

		    if buy_shop_choice == "W":
		    	Weapons_buy = [item for item in ShiningSellListWeapons if isinstance(item, Weapon)]

		    	if not Weapons_buy:
		    		print("I don't have any weapons to sell!")
		    		break

		    	print("Which weapon would you like to buy?")

		    	for i,item in enumerate(Weapons_buy,1):
		    		print("{}.{}".format(i,item))
		    	valid=False
		    	while not valid:
		    		weapon_buy_choice = input("> ")
		    		try:
			    		Player.inventory.append(Weapons_buy[int(weapon_buy_choice)-1])
			    		buy_val = item.value * Player.buy_mod
			    		Player.gold -= buy_val
			    		print("You bought a ", Weapons_buy[int(weapon_buy_choice)-1])
			    		valid = True

			    	except(ValueError,IndexError):
			    		break

		    if buy_shop_choice == "A":
		    	Armours_buy = [item for item in ShiningSellListArmours if isinstance(item, Armour)]

		    	if not Armours_buy:
		    		print("I don't have any armours to sell!")
		    		break

		    	print("Which armour would you like to buy?")

		    	for i,item in enumerate(Armours_buy,1):
		    		print("{}.{}".format(i,item))
		    	valid=False
		    	while not valid:
		    		armour_buy_choice = input("> ")
		    		try:
			    		Player.inventory.append(Armours_buy[int(armour_buy_choice)-1])
			    		buy_val = item.value * Player.buy_mod
			    		Player.gold -= buy_val
			    		print("you bought a ", Armours_buy[int(armour_buy_choice)-1])
			    		valid = True

			    	except(ValueError,IndexError):
			    		break

		    if buy_shop_choice == "E":
		    	shop_choice

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
			break

		else:
			pass
			

# Tarmalune Trade House - shop with valuables and misc
def Tarmalune(Player):
	print("NOT STARTED - Tarmalune Trade House")

# House of Knowledge - Temple to heal wounds for money
def HouseOfKnowledge(Player):
	while not Player.game_over:

		print("")
		print(f"You currently have {Player.gold} gold.")
		print(f"You currently have {Player.current_hp} hp")
		print("")
		print("Welcome to the House of Knowledge, the temple to Oghma and the great library.")
		print("What can we help you with?")

		shop_choice = check_menu_range(" ", ["Healing 10 HP (50 gold)", "Blessing", "Curse Removal", "Leave"])

		if shop_choice == 0:
			heal=10
			Player.current_hp=min(Player.max_hp,Player.current_hp+heal)
			Player.gold -= 50
			print( "Priests use their knowledge and spells to heal you.")
			print("Your health is", str(Player.current_hp))
			input("Press any key to continue")
			

		if shop_choice == 1:
			print("NOT STARTED - blessing to attributes?")

		if shop_choice == 2:
			print("NOT STARTED - remove the curse?")

		if shop_choice == 3:
			break


# Shining Serpent Inn - Inn with drinks(buy one to hear gossip) and a bed to rest (heal)
def ShiningSerpent(Player):
	print("Shining Serpent Inn")

# House of a Thousand Faces - Headquarters of the Harpers - Quests?
def HouseOfFaces(Player):
	print("House of a Thousand Faces")

# Dannar's Mechanical Marvels - Artifacts shop
def DannarsMechanical(Player):
	print("Dannar's Mechanical Marvels")

# Maskado's Maps and Legends - shop selling rumors, maps and legends
def MaskadosMaps(Player):
	print("Maskado's Maps and Legends")

# Cloak Tower - Wizard tower
def CloakTower(Player):
	print("Cloak Tower")