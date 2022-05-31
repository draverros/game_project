from tracemalloc import start
from click import prompt
import cities
import player
import items
import monsters
import locations
import lists

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
            help_menu()  # placeholder
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
    #os.system('clear')

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
    # myPlayer.charisma = myPlayer.charisma_roll + myPlayer.charsma_profession + myPlayer.charisma_race

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

    # myPlayer.hp = myPlayer.hp_profession + myPlayer.constitution_mod
    # myPlayer.mp = 0

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
    #         myPlayer.charisma = myPlayer.charisma_roll + myPlayer.charsma_profession + myPlayer.charisma_race

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

    while not myPlayer.game_over:
        choice = check_menu_range("> ", city_nev.neverwinter_menu)

        def show_inventory(inventory_list):
            if len(inventory_list) < 1:
                print("Inventory is empty.")
                return
            uniq_inventory_list = list(set(inventory_list))
            for i in range(len(uniq_inventory_list)):
                print(
                    str(i) + ") " + str(uniq_inventory_list[i]) + "(" + str(inventory_list.count(uniq_inventory_list[i]))
                    + ")")

        if choice == 0:
            print(f"Your statistics are:\n")
            print(f"Strength: {myPlayer.strength}\n"
                  f"Dexterity: {myPlayer.dexterity}\n"
                  f"Intelligence: {myPlayer.intelligence}\n"
                  f"Constitution: {myPlayer.constitution}\n"
                  f"Charisma: {myPlayer.charisma}\n"
                  f"HP: {myPlayer.hp}.\n")
            print()

        elif choice == 1:
            print(f"Your inventory contains:")
            show_inventory(myPlayer.inventory)  
            print()
            print(f"You have {myPlayer.gold} gold")
            print()
            print(f"Your weapon is {myPlayer.equipped_weapon.name}")
            print(f"Your armour is {myPlayer.equipped_armour.name}")
            print()
            print("Would you like to change your weapon(W) or armour(A)?")
            choice = input("> ").upper()
            if choice == ("W"):

                Weapons = [item for item in myPlayer.inventory if isinstance (item, Weapon)]

                if not Weapons:
                    print("You have no weapons to equip")
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

        elif choice == 2:
                print(f"You currently have {myPlayer.gold} gold.")
                shop_choice = check_menu_range("Welcome, traveller, to the Shining Knight Arms and Armour, "
                                              "the finest weapons and amour in the whole Neverwinter! Are you buying "
                                              "or selling?", ["Buy", "Sell", "Show Inventory"], True)
                if shop_choice == -1:
                    print("error")
                elif shop_choice == 0:
                    # Rebuild the below to print the list of items
                    buy_choice = check_menu_range("What would you like to buy?", lists.shining[0])
                    if myPlayer.gold - lists.shining[1][buy_choice] >= 0:
                        myPlayer.inventory.append(lists.shining[buy_choice])
                        myPlayer.gold -= lists.shining[1][buy_choice]
                    # buy_choice = check_menu_range("What would you like to buy?"list.shini)

                elif shop_choice == 1:
                    sell_choice = check_menu_range("What would you like to sell?", )
                elif shop_choice == 2:
                    show_inventory(myPlayer.inventory)

title_screen()



























