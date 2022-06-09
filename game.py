from tracemalloc import start
from click import prompt
import cities
import player
from items import*
import monsters
import locations
import lists
from spells import*

import random
import sys
import os
import time


# Title Screen #
def title_screen_selections():
    option = input("> ")
    if option.lower() == "play":
        setup_game()
    elif option.lower() == "help":
        help_menu()
    elif option.lower() == "quit":
        sys.exit()
    while option.lower() not in ['play', 'help', 'quit']:
        print("Please enter a valid command.")
        option = input("> ")
        if option.lower() == "play":
            setup_game()
        elif option.lower() == "help":
            help_menu()
        elif option.lower() == "quit":
            sys.exit()

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

def title_screen():
    os.system('clear')
    print('############################')
    print('# Welcome to the Text RPG! #')
    print('############################')
    print('          - Play -          ')
    print('          - Help -          ')
    print('          - Quit -          ')
    print('      Copyright 2022 Tom    \n')
    title_screen_selections()


def help_menu():
    os.system('clear')
    print('###########################')
    print('- Use up, down, left, right to move -')
    print('- Type your commands to do them -')
    print('- Use look to inspect something -')
    print('###########################')
    print()
    print('          - Play -          ')
    print('          - Help -          ')
    print('          - Quit -          \n')
    print()
    title_screen_selections()


myPlayer = player.Player()


def main_game_loop():
    while myPlayer.game_over is False:
        prompt()

def setup_game():
    os.system('clear')

    # # Player Name
    # question1 = "What is your name, noble warrior?\n"
    # for character in question1:
    #     sys.stdout.write(character)
    #     sys.stdout.flush()
    #     time.sleep(0.05)
    # player_name = input("> ")
    # print()
    # myPlayer.name = player_name

    # # Player Race
    # question2 = "What is your race, noble warrior?\n"
    # question2added = "You can play as a human, dwarf, elf or tiefling.\n"

    # for character in question2:
    #     sys.stdout.write(character)
    #     sys.stdout.flush()
    #     time.sleep(0.05)
    # for character in question2added:
    #     sys.stdout.write(character)
    #     sys.stdout.flush()
    #     time.sleep(0.03)

    # print()
    # print("Human: +2 Strength\n")
    # print("Dwarf: +2 Constitution\n")
    # print("Elf: +2 Dexterity\n")
    # print("Tiefling: +2 Intelligence\n")

    # player_race = input("> ")
    # valid_races = ["human", "dwarf", "elf", "tiefling"]

    # if player_race.lower() in valid_races:
    #     myPlayer.race = player_race
    #     print(f"So you are a {player_race}, huh? Interesting.\n")
    # while player_race.lower() not in valid_races:
    #     print("Please try again.")
    #     player_race = input("> ")
    #     if player_race.lower() in valid_races:
    #         myPlayer.race = player_race
    #         print(f"So you are a {player_race}, huh? Interesting.\n")

    # # Player class
    # question3 = "What do you specialise in, noble warrior?\n"
    # question3added = "You can play as a fighter, paladin, rouge or wizard.\n"
    # for character in question3:
    #     sys.stdout.write(character)
    #     sys.stdout.flush()
    #     time.sleep(0.05)
    # for character in question3added:
    #     sys.stdout.write(character)
    #     sys.stdout.flush()
    #     time.sleep(0.03)

    # print()
    # print("Fighter: +2 Strength\n")
    # print("Paladin: +2 Constitution\n")
    # print("Rouge: +2 Dexterity\n")
    # print("Wizard: +2 Intelligence\n")

    # player_profession = input("> ")
    # valid_professions = ['fighter', 'paladin', 'rouge', 'wizard']

    # if player_profession.lower() in valid_professions:
    #     myPlayer.profession = player_profession
    #     print(f"A {player_profession}, ey? In that case, I wish you luck. You will need it.\n")
    #     print(f"")
    # while player_profession.lower() not in valid_professions:
    #     print("Please try again.")
    #     player_profession = input("> ")
    #     if player_profession.lower() in valid_professions:
    #         myPlayer.profession = player_profession
    #         print(f"A {player_profession}, ey? In that case, I wish you luck. You will need it.\n")

    # # Player Roll Stats
    # myPlayer.strength_roll = random.randint(8, 18)
    # myPlayer.dexterity_roll = random.randint(8, 18)
    # myPlayer.intelligence_roll = random.randint(8, 18)
    # myPlayer.constitution_roll = random.randint(8, 18)
    # myPlayer.charisma_roll = random.randint(8, 18)
    
    # # Player starting equipement
    # if myPlayer.profession == 'fighter':
    #     myPlayer.equipped_weapon = Sword()
    #     myPlayer.equipped_armour = LeatherArmour()
    #     myPlayer.equipped_ring = WeakRingStr()
    #     myPlayer.equipped_amulet = WeakAmuletStr()
    #     myPlayer.gold = 160
    # elif myPlayer.profession == 'paladin':
    #     myPlayer.equipped_weapon = Sword()
    #     myPlayer.equipped_armour = HideArmour()
    #     myPlayer.equipped_ring = WeakRingCon()
    #     myPlayer.equipped_amulet = WeakAmuletCha()
    #     myPlayer.gold = 110
    # elif myPlayer.profession == 'rouge':
    #     myPlayer.equipped_weapon = Dagger()
    #     myPlayer.equipped_armour = LeatherArmour()
    #     myPlayer.equipped_ring = WeakRingDex()
    #     myPlayer.equipped_amulet = WeakAmuletDex()
    #     myPlayer.gold = 90
    # elif myPlayer.profession == 'wizard':
    #     myPlayer.equipped_weapon = Quarterstaff()
    #     myPlayer.equipped_armour = Cloak()
    #     myPlayer.equipped_ring = WeakRingInt()
    #     myPlayer.equipped_amulet = WeakAmuletInt()
    #     myPlayer.gold = 60


    # # Player Class Stats
    # if myPlayer.profession == 'fighter':
    #     myPlayer.strength_profession = 2
    #     myPlayer.dexterity_profession = 0
    #     myPlayer.intelligence_profession = 0
    #     myPlayer.constitution_profession = 0
    #     myPlayer.charisma_profession = 0
    #     myPlayer.hp_profession = 10
    #     myPlayer.mp_profession = 0
    # elif myPlayer.profession == 'paladin':
    #     myPlayer.strength_profession = 0
    #     myPlayer.dexterity_profession = 0
    #     myPlayer.intelligence_profession = 0
    #     myPlayer.constitution_profession = 2
    #     myPlayer.charisma_profession = 0
    #     myPlayer.hp_profession = 10
    #     myPlayer.mp_profession = 0
    # elif myPlayer.profession == 'rouge':
    #     myPlayer.strength_profession = 0
    #     myPlayer.dexterity_profession = 2
    #     myPlayer.intelligence_profession = 0
    #     myPlayer.constitution_profession = 0
    #     myPlayer.charsma_profession = 0
    #     myPlayer.hp_profession = 8
    #     myPlayer.mp_profession = 0
    # elif myPlayer.profession == 'wizard':
    #     myPlayer.strength_profession = 0
    #     myPlayer.dexterity_profession = 0
    #     myPlayer.intelligence_profession = 2
    #     myPlayer.constitution_profession = 0
    #     myPlayer.charsma_profession = 0
    #     myPlayer.hp_profession = 6
    #     myPlayer.mp_profession = 0

    # # Player Race Stats
    # if myPlayer.race == 'human':
    #     myPlayer.strength_race = 2
    #     myPlayer.dexterity_race = 0
    #     myPlayer.intelligence_race = 0
    #     myPlayer.constitution_race = 0
    #     myPlayer.charisma_race = 0
    # elif myPlayer.race == 'dwarf':
    #     myPlayer.strength_race = 0
    #     myPlayer.dexterity_race = 0
    #     myPlayer.intelligence_race = 0
    #     myPlayer.constitution_race = 2
    #     myPlayer.charisma_racer = 2
    # elif myPlayer.race == 'elf':
    #     myPlayer.strength_race = 0
    #     myPlayer.dexterity_race = 2
    #     myPlayer.intelligence_race = 0
    #     myPlayer.constitution_race = 0
    #     myPlayer.charisma_race = 0
    # elif myPlayer.race == 'tiefling':
    #     myPlayer.strength_race = 0
    #     myPlayer.dexterity_race = 0
    #     myPlayer.intelligence_race = 2
    #     myPlayer.constitution_race = 0
    #     myPlayer.charisma_race = 0

    # # Player Stats Final
    # myPlayer.strength = myPlayer.strength_roll + myPlayer.strength_profession + myPlayer.strength_race
    # myPlayer.dexterity = myPlayer.dexterity_roll + myPlayer.dexterity_profession + myPlayer.dexterity_race
    # myPlayer.intelligence = myPlayer.intelligence_roll + myPlayer.intelligence_profession + myPlayer.intelligence_race
    # myPlayer.constitution = myPlayer.constitution_roll + myPlayer.constitution_profession + myPlayer.constitution_race
    # myPlayer.charisma = myPlayer.charisma_roll + myPlayer.charisma_profession + myPlayer.charisma_race

    # # Player HP modifiers
    # if myPlayer.constitution_roll + myPlayer.constitution_race + myPlayer.constitution_profession < 10:
    #     myPlayer.constitution_mod = -1
    # elif myPlayer.constitution_roll + myPlayer.constitution_race + myPlayer.constitution_profession < 12:
    #     myPlayer.constitution_mod = 0
    # elif myPlayer.constitution_roll + myPlayer.constitution_race + myPlayer.constitution_profession < 14:
    #     myPlayer.constitution_mod = 1
    # elif myPlayer.constitution_roll + myPlayer.constitution_race + myPlayer.constitution_profession < 16:
    #     myPlayer.constitution_mod = 2
    # elif myPlayer.constitution_roll + myPlayer.constitution_race + myPlayer.constitution_profession < 18:
    #     myPlayer.constitution_mod = 3
    # elif myPlayer.constitution_roll + myPlayer.constitution_race + myPlayer.constitution_profession < 20:
    #     myPlayer.constitution_mod = 4
    # elif myPlayer.constitution_roll + myPlayer.constitution_race + myPlayer.constitution_profession < 22:
    #     myPlayer.constitution_mod = 5
    # elif myPlayer.constitution_roll + myPlayer.constitution_race + myPlayer.constitution_profession < 24:
    #     myPlayer.constitution_mod = 6
    # elif myPlayer.constitution_roll + myPlayer.constitution_race + myPlayer.constitution_profession < 26:
    #     myPlayer.constitution_mod = 7
    # elif myPlayer.constitution_roll + myPlayer.constitution_race + myPlayer.constitution_profession < 28:
    #     myPlayer.constitution_mod = 8
    # elif myPlayer.constitution_roll + myPlayer.constitution_race + myPlayer.constitution_profession < 30:
    #     myPlayer.constitution_mod = 9
    # elif myPlayer.constitution_roll + myPlayer.constitution_race + myPlayer.constitution_profession == 30:
    #     myPlayer.constitution_mod = 10

    # myPlayer.current_hp = myPlayer.hp_profession + myPlayer.constitution_mod
    # myPlayer.max_hp = myPlayer.hp_profession + myPlayer.constitution_mod
    # myPlayer.current_mp = 0
    # myPlayer.max_mp = 100

    # os.system('clear')
    # print(f"Your statistics are:\n")
    # print(f"Strength: {myPlayer.strength}\n"
    #       f"Dexterity: {myPlayer.dexterity}\n"
    #       f"Intelligence: {myPlayer.intelligence}\n"
    #       f"Constitution: {myPlayer.constitution}\n"
    #       f"Charisma: {myPlayer.charisma}\n"
    #       f"HP: {myPlayer.hp}.\n")

    # # Statistics acceptance or reroll
    # ask_again = True
    # def reroll_def():
    #     global ask_again
    # while ask_again:
    #     reroll_def()
    #     print("Would you like to roll for the stats again?? (Yes/No)")
    #     player_reroll = input("> ")
    #     if player_reroll.lower() == "yes":
    #         ask_again = True
    #         myPlayer.strength_roll = random.randint(8, 18)
    #         myPlayer.dexterity_roll = random.randint(8, 18)
    #         myPlayer.intelligence_roll = random.randint(8, 18)
    #         myPlayer.constitution_roll = random.randint(8, 18)
    #         myPlayer.charisma_roll = random.randint(8, 18)

    #         myPlayer.strength = myPlayer.strength_roll + myPlayer.strength_profession + myPlayer.strength_race
    #         myPlayer.dexterity = myPlayer.dexterity_roll + myPlayer.dexterity_profession + myPlayer.dexterity_race
    #         myPlayer.intelligence = myPlayer.intelligence_roll + myPlayer.intelligence_profession + myPlayer.intelligence_race
    #         myPlayer.constitution = myPlayer.constitution_roll + myPlayer.constitution_profession + myPlayer.constitution_race
    #         myPlayer.charisma = myPlayer.charisma_roll + myPlayer.charisma_profession + myPlayer.charisma_race

    #         if myPlayer.constitution_roll + myPlayer.constitution_race + myPlayer.constitution_profession < 10:
    #             myPlayer.constitution_mod = -1
    #         elif myPlayer.constitution_roll + myPlayer.constitution_race + myPlayer.constitution_profession < 12:
    #             myPlayer.constitution_mod = 0
    #         elif myPlayer.constitution_roll + myPlayer.constitution_race + myPlayer.constitution_profession < 14:
    #             myPlayer.constitution_mod = 1
    #         elif myPlayer.constitution_roll + myPlayer.constitution_race + myPlayer.constitution_profession < 16:
    #             myPlayer.constitution_mod = 2
    #         elif myPlayer.constitution_roll + myPlayer.constitution_race + myPlayer.constitution_profession < 18:
    #             myPlayer.constitution_mod = 3
    #         elif myPlayer.constitution_roll + myPlayer.constitution_race + myPlayer.constitution_profession < 20:
    #             myPlayer.constitution_mod = 4
    #         elif myPlayer.constitution_roll + myPlayer.constitution_race + myPlayer.constitution_profession < 22:
    #             myPlayer.constitution_mod = 5
    #         elif myPlayer.constitution_roll + myPlayer.constitution_race + myPlayer.constitution_profession < 24:
    #             myPlayer.constitution_mod = 6
    #         elif myPlayer.constitution_roll + myPlayer.constitution_race + myPlayer.constitution_profession < 26:
    #             myPlayer.constitution_mod = 7
    #         elif myPlayer.constitution_roll + myPlayer.constitution_race + myPlayer.constitution_profession < 28:
    #             myPlayer.constitution_mod = 8
    #         elif myPlayer.constitution_roll + myPlayer.constitution_race + myPlayer.constitution_profession < 30:
    #             myPlayer.constitution_mod = 9
    #         elif myPlayer.constitution_roll + myPlayer.constitution_race + myPlayer.constitution_profession == 30:
    #             myPlayer.constitution_mod = 10

    #         myPlayer.hp = myPlayer.hp_profession + myPlayer.constitution_mod
    #         myPlayer.mp = 0

    #         print(f"Your statistics are:\n")
    #         print(f"Strength: {myPlayer.strength}\n"
    #               f"Dexterity: {myPlayer.dexterity}\n"
    #               f"Intelligence: {myPlayer.intelligence}\n"
    #               f"Constitution: {myPlayer.constitution}\n"
    #               f"Charisma: {myPlayer.charisma}\n"
    #               f"HP: {myPlayer.hp}.\n")

    #     elif player_reroll.lower() == "no":
    #         ask_again = False





    os.system('clear')
    city_nev = cities.Neverwinter()
    #print(f"Welcome, {player_name}. You are a {player_race}, a {player_profession}.")
    myPlayer.max_hp = 700
    myPlayer.current_hp = 10
    myPlayer.max_mp = 100
    myPlayer.current_mp = 10
    myPlayer.charisma = 25

    if myPlayer.charisma == 15:
        myPlayer.buy_mod = 1

    elif myPlayer.charisma == 14:
        myPlayer.buy_mod = 0.95

    elif myPlayer.charisma == 13:
        myPlayer.buy_mod = 0.9

    elif myPlayer.charisma == 12:
        myPlayer.buy_mod = 0.85

    elif myPlayer.charisma == 11:
        myPlayer.buy_mod = 0.8

    elif myPlayer.charisma == 10:
        myPlayer.buy_mod = 0.75

    elif myPlayer.charisma == 9:
        myPlayer.buy_mod = 0.7

    elif myPlayer.charisma == 8:
        myPlayer.buy_mod = 0.65

    elif myPlayer.charisma <= 7:
        myPlayer.buy_mod = 0.6

    elif myPlayer.charisma == 16:
        myPlayer.buy_mod = 1.05

    elif myPlayer.charisma == 17:
        myPlayer.buy_mod = 1.1

    elif myPlayer.charisma == 18:
        myPlayer.buy_mod = 1.15

    elif myPlayer.charisma == 19:
        myPlayer.buy_mod = 1.2

    elif myPlayer.charisma == 20:
        myPlayer.buy_mod = 1.25

    elif myPlayer.charisma == 21:
        myPlayer.buy_mod = 1.3

    elif myPlayer.charisma == 22:
        myPlayer.buy_mod = 1.35

    elif myPlayer.charisma == 23:
        myPlayer.buy_mod = 1.4

    elif myPlayer.charisma == 24:
        myPlayer.buy_mod = 1.45

    elif myPlayer.charisma >= 25:
        myPlayer.buy_mod = 1.5

    while not myPlayer.game_over:
        choice = check_menu_range(" ",city_nev.neverwinter_menu,)

        def show_inventory(inventory_list):
            if len(inventory_list) < 1:
                print("Inventory is empty.")
                return
            uniq_inventory_list = list(set(inventory_list))
            for i in range(len(uniq_inventory_list)):
                print(
                    str(i) + ") " + str(uniq_inventory_list[i]) + "(" + str(inventory_list.count(uniq_inventory_list[i]))
                    + ")")

        if choice == 0: # Print statistics
            print(f"Your statistics are:\n")
            print(f"Strength: {myPlayer.strength}\n"
                  f"Dexterity: {myPlayer.dexterity}\n"
                  f"Intelligence: {myPlayer.intelligence}\n"
                  f"Constitution: {myPlayer.constitution}\n"
                  f"Charisma: {myPlayer.charisma}\n"
                  f"HP: {myPlayer.current_hp}/{myPlayer.max_hp}\n"
                  f"MP: {myPlayer.current_mp}/{myPlayer.max_mp}\n"
                  f"BuyMod: {myPlayer.buy_mod}\n"
                  f"BuyMod: {myPlayer.sell_mod}\n")

            print()

        elif choice == 1: #Print inventory + change equipement
            print(f"Your inventory contains:")
            show_inventory(myPlayer.inventory)
            print()
            print(f"You have {myPlayer.gold} gold")
            print()
            print(f"Your weapon is {myPlayer.equipped_weapon.name}")
            print(f"Your armour is {myPlayer.equipped_armour.name}")
            print(f"You are currently wearing a {myPlayer.equipped_ring.name}")
            print(f"You are currently wearing a {myPlayer.equipped_amulet.name}")
            #print(f"You are currently wearing a {myPlayer.equipped_artifact.name}")
            print()
            print("Would you like to change your weapon(W), armour(A) or other(O)? (Press Enter to leave)")
            choice = input("> ").upper()
            if choice == ("W"):

                Weapons = [item for item in myPlayer.inventory if isinstance (item, Weapon)]

                if not Weapons:
                    print("You have no weapons to equip.")
                    break

                print("Choose a weapon to equip: ")

                for i,item in enumerate(Weapons,1):
                    print("{}. {}".format(i,item))

                valid = False
                while not valid:
                    choice = input("> ")
                    try:
                        bob=myPlayer.equipped_weapon # fix bug that replicate item if error
                        myPlayer.inventory.remove(Weapons[int(choice)-1])
                        myPlayer.equipped_weapon=Weapons[int(choice)-1]
                        myPlayer.inventory.append(bob)
                        print("You arm yourself with :",Weapons[int(choice)-1])
                        valid=True

                    except (ValueError,IndexError):
                        print("Invalid choice, try again ")

            elif choice == ("A"):

                Armours = [item for item in myPlayer.inventory if isinstance(item, Armour)]

                if not Armours:
                    print("You have no armour to equip.")
                    break

                print("Choose the armour to equip: ")

                for i,item in enumerate(Armours,1):
                    print("{}.{}".format(i,item))

                valid=False
                while not valid:
                    choice = input("")
                    try:
                        bob=myPlayer.equipped_armour # fix bug that replace item if error
                        myPlayer.inventory.remove(Armours[int(choice)-1])
                        myPlayer.equipped_armour = Armours[int(choice)-1]
                        myPlayer.inventory.append(bob)
                        print("You start wearing: ", Armours[int(choice)-1])
                        valid = True

                    except (ValueError,IndexError):
                        print("Invalid choice, try again.")

            elif choice == ("O"):
                print("Would you like to change your ring(R), amulet(A) or artifact(M)?")
                choice = input("> ").upper()

                if choice == ("R").upper():

                    Rings = [item for item in myPlayer.inventory if isinstance (item, Ring)]

                    if not Rings:
                        print("You have no rings to equip.")
                        break

                    print("Choose a ring to equip: ")

                    for i,item in enumerate(Rings,1):
                        print("{}. {}".format(i,item))

                    valid = False
                    while not valid:
                        choice = input("> ")
                        try:
                            bob=myPlayer.equipped_ring # fix bug that replicate item if error
                            myPlayer.inventory.remove(Rings[int(choice)-1])
                            myPlayer.equipped_ring=Rings[int(choice)-1]
                            myPlayer.inventory.append(bob)
                            print("You arm yourself with :",Rings[int(choice)-1])
                            valid=True

                        except (ValueError,IndexError):
                            print("Invalid choice, try again ")

                elif choice == ("A").upper():

                    Amulets = [item for item in myPlayer.inventory if isinstance (item, Amulet)]

                    if not Amulets:
                        print("You have no amulets to equip.")
                        break

                    print("Choose the amulet to equip: ")

                    for i,item in enumerate(Amulets,1):
                        print("{}. {}".format(i,item))

                    valid = False
                    while not valid:
                        choice = input("> ")
                        try:
                            bob=myPlayer.equipped_amulet # fix bug that replicate item if error
                            myPlayer.inventory.remove(Amulets[int(choice)-1])
                            myPlayer.equipped_amulet=Amulets[int(choice)-1]
                            myPlayer.inventory.append(bob)
                            print("You arm yourself with :",Amulets[int(choice)-1])
                            valid=True

                        except (ValueError,IndexError):
                            print("Invalid choice, try again ")


        elif choice == 2:
            locations.ShiningKnight(myPlayer)

        elif choice == 3:
            locations.Tarmalune(myPlayer)
            print("")

        elif choice == 4:
            locations.HouseOfKnowledge(myPlayer)
            print("")

        elif choice == 5:
            locations.ShiningSerpent(myPlayer)
            print("")

        elif choice == 6:
            locations.HouseOfFaces(myPlayer)
            print("")

        elif choice == 7:
            locations.DannarsMechanical(myPlayer)
            print("")

        elif choice == 8:
            locations.MaskadosMaps(myPlayer)
            print("")

        elif choice == 9:
            locations.CloakTower(myPlayer)
            print("")

title_screen()
