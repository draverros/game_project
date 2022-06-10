from items import *
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

def shining_knight(Player):
    while not Player.game_over:
        print("")
        print(f"You currently have {Player.gold} gold.")
        print("")

        shining_sell_list_weapons = [Club(), Sword(), Dagger(), Handaxe(), Longsword(), Mace(), Quarterstaff(),
                                     Warhammer()]
        shining_sell_list_armours = [Cloak(), BrestplateArmour(), ChainMailArmour(), ChainShirtArmour(),
                                     HalfPlateArmour(), HideArmour(), LeatherArmour(), PlateArmour(), RingMailArmour(),
                                     ScaleMailArmour(), PaddedArmour(), SplintArmour(), StuddedLeatherArmour()]

        shop_choice = check_menu_range("Welcome, traveller, to the Shining Knight Arms and Armour, "
                                       "the finest weapons and amour in the whole Neverwinter! Are you buying "
                                       "or selling?", ["Buy", "Sell", "Exit"], True)

        if shop_choice == -1:
            print("error")

        if shop_choice == 0:
            print("What would you like to buy, Weapon(W) or Armour(A). Exit (E)")
            buy_shop_choice = input("Choice: ").upper()

            if buy_shop_choice == "W":
                weapons_buy = [item for item in shining_sell_list_weapons if isinstance(item, Weapon)]

                if not weapons_buy:
                    print("I don't have any weapons to sell!")
                    break

                print("Which weapon would you like to buy?")

                for i, item in enumerate(weapons_buy, 1):
                    print("{}.{}".format(i, item))
                valid = False
                while not valid:
                    weapon_buy_choice = input("> ")
                    try:
                        Player.inventory.append(weapons_buy[int(weapon_buy_choice) - 1])
                        buy_val = item.value * Player.buy_mod
                        Player.gold -= round(buy_val, 2)
                        print("You bought a ", weapons_buy[int(weapon_buy_choice) - 1])
                        valid = True

                    except(ValueError, IndexError):
                        break

            if buy_shop_choice == "A":
                armours_buy = [item for item in shining_sell_list_armours if isinstance(item, Armour)]

                if not armours_buy:
                    print("I don't have any armours to sell!")
                    break

                print("Which armour would you like to buy?")

                for i, item in enumerate(armours_buy, 1):
                    print("{}.{}".format(i, item))
                valid = False
                while not valid:
                    armour_buy_choice = input("> ")
                    try:
                        Player.inventory.append(armours_buy[int(armour_buy_choice) - 1])
                        buy_val = item.value * Player.buy_mod
                        Player.gold -= round(buy_val, 2)
                        print("you bought a ", armours_buy[int(armour_buy_choice) - 1])
                        valid = True

                    except(ValueError, IndexError):
                        break

            if buy_shop_choice == "E":
                break

        elif shop_choice == 1:
            if len(Player.inventory) > 0:
                print("What would you like to sell? A weapon(W), an armour(A) or other(O)?")
                sell_choice = input("Choice: ").upper()

                if sell_choice == "W":
                    weapons_sell = [item for item in Player.inventory if isinstance(item, Weapon)]

                    if not weapons_sell:
                        print("You don't have any weapons to sell.")
                        break

                    print("Which weapon would you like to sell?")

                    for i, item in enumerate(weapons_sell, 1):
                        print("{}.{}".format(i, item))
                    valid = False
                    while not valid:
                        weapon_sell_choice = input("> ")
                        try:
                            Player.inventory.remove(weapons_sell[int(weapon_sell_choice) - 1])
                            sell_val = item.value * Player.sell_mod
                            Player.gold += round(sell_val, 2)
                            print("You sold a ", weapons_sell[int(weapon_sell_choice) - 1])
                            valid = True

                        except(ValueError, IndexError):
                            break

                elif sell_choice == "A":
                    armours_sell = [item for item in Player.inventory if isinstance(item, Armour)]

                    if not armours_sell:
                        print("You don't have any armours to sell.")
                        break

                    print("Which armour would you like to sell?")

                    for i, item in enumerate(armours_sell, 1):
                        print("{}.{}".format(i, item))
                    valid = False
                    while not valid:
                        armour_sell_choice = input("> ")
                        try:
                            Player.inventory.remove(armours_sell[int(armour_sell_choice) - 1])
                            sell_val = item.value * Player.sell_mod
                            Player.gold += round(sell_val, 2)
                            print("You sold a ", armours_sell[int(armour_sell_choice) - 1])
                            valid = True

                        except(ValueError, IndexError):
                            break

                elif sell_choice == "O":
                    print("Would you like to sell a ring(R), amulet(A) or valuable(V)")
                    other_sell_choice = input("Choice: ").upper()

                    if other_sell_choice == "R":
                        rings_sell = [item for item in Player.inventory if isinstance(item, Ring)]

                        if not rings_sell:
                            print("You don't have any rings to sell.")
                            break

                        print("Which ring would you like to sell?")

                        for i, item in enumerate(rings_sell, 1):
                            print("{}.{}".format(i, item))
                        valid = False
                        while not valid:
                            ring_sell_choice = input("> ")
                            try:
                                Player.inventory.remove(rings_sell[int(ring_sell_choice) - 1])
                                sell_val = item.value * Player.sell_mod
                                Player.gold += round(sell_val, 2)
                                print("You sold a ", rings_sell[int(ring_sell_choice) - 1])
                                valid = True

                            except(ValueError, IndexError):
                                break

                    elif other_sell_choice == "A":
                        amulets_sell = [item for item in Player.inventory if isinstance(item, Amulet)]

                        if not amulets_sell:
                            print("You don't have any amulets to sell.")
                            break

                        print("Which amulet would you like to sell?")

                        for i, item in enumerate(amulets_sell, 1):
                            print("{}.{}".format(i, item))
                        valid = False
                        while not valid:
                            amulet_sell_choice = input("> ")
                            try:
                                Player.inventory.remove(amulets_sell[int(amulet_sell_choice) - 1])
                                sell_val = item.value * Player.sell_mod
                                Player.gold += round(sell_val, 2)
                                print("You sold a ", amulets_sell[int(amulet_sell_choice) - 1])
                                valid = True

                            except(ValueError, IndexError):
                                break

                    elif other_sell_choice == "V":
                        valuables_sell = [item for item in Player.inventory if isinstance(item, Valuable)]

                        if not valuables_sell:
                            print("You don't have any valuables to sell.")
                            break

                        print("Which item would you like to sell?")

                        for i, item in enumerate(valuables_sell, 1):
                            print("{}.{}".format(i, item))
                        valid = False
                        while not valid:
                            valuable_sell_choice = input("> ")
                            try:
                                Player.inventory.remove(valuables_sell[int(valuable_sell_choice) - 1])
                                sell_val = item.value * Player.sell_mod
                                Player.gold += round(sell_val, 2)
                                print("You sold a ", valuables_sell[int(valuable_sell_choice) - 1], " for ", sell_val)
                                valid = True

                            except(ValueError, IndexError):
                                break

        elif shop_choice == 2:
            break

        else:
            pass


# Tarmalune Trade House - shop with valuables and misc
def tarmalune(Player):
    print("NOT STARTED - Tarmalune Trade House")


# House of Knowledge - Temple to heal wounds for money
def house_of_knowledge(Player):
    while not Player.game_over:

        print("")
        print(f"You currently have {Player.gold} gold.")
        print(f"You currently have {Player.current_hp} hp")
        print("")
        print("Welcome to the House of Knowledge, the temple to Oghma and the great library.")
        print("What can we help you with?")

        shop_choice = check_menu_range(" ", ["Healing 10 HP (50 gold)", "Blessing", "Curse Removal", "Leave"])

        if shop_choice == 0:
            heal = 10
            Player.current_hp = min(Player.max_hp, Player.current_hp + heal)
            Player.gold -= 50
            print("Priests use their knowledge and spells to heal you.")
            print("Your health is", str(Player.current_hp))
            input("Press any key to continue")

        if shop_choice == 1:
            print("NOT STARTED - blessing to attributes?")

        if shop_choice == 2:
            print("NOT STARTED - remove the curse?")

        if shop_choice == 3:
            break


# Shining Serpent Inn - Inn with drinks(buy one to hear gossip) and a bed to rest (heal)
def shining_serpent(Player):
    while not Player.game_over:

        print("")
        print(f"You currently have {Player.gold} gold.")
        print(f"You currently have {Player.current_hp} hp")
        print("")
        print("Welcome to the Shining Serpent, the best inn the whole of Neverwinter.")
        print("What can we help you with?")

        shop_choice = check_menu_range(" ", ["Buy a drink (10 gold)", "Rest (100 gold)", "Leave"])

        if shop_choice == 0:
            print("Not ready yet")

        if shop_choice == 1:
            heal = 10000
            Player.current_hp = min(Player.max_hp, Player.current_hp + heal)
            Player.current_mp = min(Player.max_mp, Player.current_mp + heal)
            Player.gold -= 100
            print("You go to bed and wake up refreshed.")
            print("Your health is now", str(Player.current_hp))
            print("Your mana is now", str(Player.current_mp))
            input("Press any key to continue")

        if shop_choice == 2:
            break


# House of a Thousand Faces - Headquarters of the Harpers - Quests?
def house_of_faces(Player):
    print("House of a Thousand Faces")


# Dannar's Mechanical Marvels - Artifacts shop
def dannars_mechanical(Player):
    print("Dannar's Mechanical Marvels")


# Maskado's Maps and Legends - shop selling rumors, maps and legends
def maskados_maps(Player):
    print("Maskado's Maps and Legends")


# Cloak Tower - Wizard tower
def cloak_tower(Player):
    print("Cloak Tower")
