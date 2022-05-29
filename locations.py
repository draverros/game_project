import items
from player import Player
import lists

club = items.Club()
crossbow = items.Crossbow()
dagger = items.Dagger()
leatherarmour = items.StuddedLeatherArmour()
brestplatearmour = items.BrestplateArmour()

myPlayer = Player()

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


# Neverwinter

# Shining Knight Arms and Armour

#class ShiningKnightArmsAndArmour:
 #   def __init__(self):
  #      self.shining_knight_buy = [club.name, crossbow.name, dagger.name, leatherarmour.name, brestplatearmour.name]
   #     self.shining_knight_buy = [club.value, crossbow.value, dagger.value, leatherarmour.value, brestplatearmour.value]

# Tarmalune Trade House

# House of Knowledge

# Shining Serpent Inn

# House of a Thousand Faces

# Dannar's Mechanical Marvels

# Maskado's Maps and Legends

# Cloak Tower

def ShiningKnightArmsAndArmour(Player):
                print(f"You currently have {myPlayer.gold} gold.")
                shop_choice = check_menu_range("Welcome, traveller, to the Shining Knight Arms and Armour, "
                                              "the finest weapons and amour in the whole Neverwinter! Are you buying "
                                              "or selling?", ["Buy", "Sell", "Show Inventory"], True)
                if shop_choice == -1:
                    print("error")
                elif shop_choice == 0:
                    buy_choice = check_menu_range("What would you like to buy?", lists.shining)
                    if myPlayer.gold - lists.shining.value[buy_choice] >= 0:
                        myPlayer.inventory.append(lists.shining[buy_choice])
                        myPlayer.gold -= lists.shining.value[buy_choice]
                elif shop_choice == 1:
                    sell_choice = check_menu_range("What would you like to sell?", )
                elif shop_choice == 2:
                    show_inventory(myPlayer.inventory)