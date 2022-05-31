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
	                              "or selling?", ["Buy", "Sell", "Show Inventory"], True)
	if shop_choice == -1:
	    print("error")
	elif shop_choice == 0:
	    print("Would you like to buy a Club or a Dagger?")
	choice = input("Choice: ").upper()
	if choice == ("C"):
		if Player.gold < 20:
			print("You can't afford it.")
		else:
		    Player.inventory.append(Club())
		    Player.gold -= 20
		    print("You got a club")
	elif choice == ("D"):
	    Player.inventory.append(Dagger())
	    print("You got a dagger")

	elif shop_choice == 1:
	    sell_choice = check_menu_range("What would you like to sell?", )
	elif shop_choice == 2:
	    show_inventory(myPlayer.inventory)

# Tarmalune Trade House

# House of Knowledge

# Shining Serpent Inn

# House of a Thousand Faces

# Dannar's Mechanical Marvels

# Maskado's Maps and Legends

# Cloak Tower