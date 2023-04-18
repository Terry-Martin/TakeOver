"""
Import time
Import random
Import google sheet
Import adapted from LoveSandwiches example
"""
import time
import random
import pyfiglet
import gspread
from google.oauth2.service_account import Credentials
from colorama import Fore, Back, Style
from colorama import just_fix_windows_console
just_fix_windows_console()
# import pyfiglet module

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]
CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("takeover")


class Character:
    """
    Create Character class to be used for player and foe
    """
    def __init__(self, cid, name, health, attack_power):
        self.cid = cid
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, health, attack_power):
        """
        Attack is health minus attack_power
        """
        health -= attack_power
        return health

    def intro(self, cid, name, health, attack_power):
        """
        Display information about character
        """
        print(f"  My name is {name}.")
        print(f"  The number {cid} is tattoed on my arm.")
        print(f"  My health is {health}.")
        print(f"  My attack power is {attack_power}.\n")


def create_player():
    """
    Create player
    """
    # Get information from google sheet for player
    player_info_all = SHEET.worksheet("player")

    # info_test = SHEET.worksheet("player").get_all_values()
    # info_test1 = SHEET.worksheet("player").row_values(3)

    # **CLEAN UP**
    player_id = player_info_all.cell(2, 1).value
    player_name = player_info_all.cell(2, 2).value
    player_health = int(player_info_all.cell(2, 3).value)
    player_attack_power = int(player_info_all.cell(2, 4).value)

    # Create player from Character class
    return Character(player_id, player_name, player_health,
                     player_attack_power)


def create_foe(foe_number):
    """
    Create foe
    """
    # Get information from google sheet for foe

    get_foe_info = SHEET.worksheet("foe").row_values(foe_number)
    foe_id = get_foe_info[0]
    foe_name = get_foe_info[1]
    foe_health = int(get_foe_info[2])
    foe_attack_power = int(get_foe_info[3])

    # Create foe from Chatacter class and send back to main function
    return Character(foe_id, foe_name, foe_health, foe_attack_power)


def start_battle(foe, player):
    """
    Start battle between player and foe
    """
    while foe.health > 0 and player.health > 0:
    
        print(Fore.RED + f"  {player.name} has dealt {player.attack_power} damage")
        print(Fore.WHITE)
        # print(Style.RESET_ALL)
        foe.health = player.attack(foe.health, player.attack_power)
        print(f"  {foe.name} has {foe.health} health remaining\n")
        if foe.health <= 0:
            print(f"  {player.name} has defeated the {foe.name}!!! \n")
            break

        print(f"  {foe.name} has dealt {foe.attack_power} damage")
        player.health = foe.attack(player.health, foe.attack_power)
        print(Fore.GREEN + f"  {player.name} has {player.health} health remaining\n")
        print(Fore.WHITE)
        if player.health <= 0:
            print(f"  The {foe.name} has defeated {player.name}!!! \n")
            print(Back.RED + "  **** GAME OVER ****")
            print(Style.RESET_ALL)
            print()
            exit()
            # break


def add_new_player_to_worksheet(new_player, player_worksheet):
    """
    Add new player to player google sheet
    """
    player_worksheet_update = SHEET.worksheet(player_worksheet)
    player_worksheet_update.append_row(new_player)


def story_intro(story_start):
    """
    Display story start
    """
    # https://pypi.org/project/colorama/
    result = pyfiglet.figlet_format("TakeOver")
    # print(Style.BRIGHT + result)
    print(result)

    print(Fore.RED + result)
   
    # print(Back.GREEN + 'and with a green background')
    # print(Style.DIM + 'and in dim text')
    print(Style.RESET_ALL)
    # print(Style.BRIGHT + 'and in bright text')
    # print(Style.RESET_ALL)
    # print(Back.BLUE)

    print("\n" + story_start[1] + "\n")
    print(story_start[2] + "\n")
    print(story_start[3] + "\n")
    print(story_start[4] + "\n")


def decision(decision_tree, player):
    """
    Testtesttest
    """
    get_text_info = SHEET.worksheet("text").col_values(2)

    if decision_tree == 1:
        while True:
            player_choice = input(get_text_info[7])

            try:
                player_choice = int(player_choice)
                break
            except ValueError:
                print("  You need to enter a number" + "\n")

        if player_choice == 1:
            foe = create_foe(3)
            foe.intro(foe.cid, foe.name, foe.health, foe.attack_power)
            start_battle(foe, player)

            foe_two = create_foe(3)
            foe_two.intro(foe_two.cid, foe_two.name, foe_two.health,
                          foe_two.attack_power)
            start_battle(foe_two, player)

            foe_three = create_foe(4)
            foe_three.intro(foe_three.cid, foe_three.name, foe_three.health,
                            foe_three.attack_power)
            start_battle(foe_three, player)
        else:
            foe = create_foe(2)
            foe.intro(foe.cid, foe.name, foe.health, foe.attack_power)
            start_battle(foe, player)

            foe_two = create_foe(2)
            foe_two.intro(foe_two.cid, foe_two.name, foe_two.health,
                          foe_two.attack_power)
            start_battle(foe_two, player)

            foe_three = create_foe(5)
            foe_three.intro(foe_three.cid, foe_three.name, foe_three.health,
                            foe_three.attack_power)
            start_battle(foe_three, player)

        print("\n" + get_text_info[8] + "\n")
        print(get_text_info[9] + "\n")

    elif decision_tree == 2:
        # Validate player input choice
        while True:
            player_choice = input(get_text_info[10])
            try:
                player_choice = int(player_choice)
                break
            except ValueError:
                print("  You need to enter a number \n")

        if player_choice == 1:
            foe = create_foe(6)
            foe.intro(foe.cid, foe.name, foe.health, foe.attack_power)
            start_battle(foe, player)
            foe_two = create_foe(7)
            foe_two.intro(foe_two.cid, foe_two.name, foe_two.health,
                          foe_two.attack_power)
            start_battle(foe_two, player)
            foe_three = create_foe(9)
            foe_three.intro(foe_three.cid, foe_three.name, foe_three.health,
                            foe_three.attack_power)
            start_battle(foe_three, player)
        else:
            foe = create_foe(6)
            foe.intro(foe.cid, foe.name, foe.health, foe.attack_power)
            start_battle(foe, player)
            foe_two = create_foe(8)
            foe_two.intro(foe_two.cid, foe_two.name, foe_two.health,
                          foe_two.attack_power)
            start_battle(foe_two, player)
            foe_three = create_foe(8)
            foe_three.intro(foe_three.cid, foe_three.name, foe_three.health,
                            foe_three.attack_power)
            start_battle(foe_three, player)

        print("\n" + get_text_info[11] + "\n")
        print(get_text_info[12] + "\n")

    elif decision_tree == 3:
        # Validate player input choice
        while True:
            player_choice = input(get_text_info[13])
            try:
                player_choice = int(player_choice)
                break
            except ValueError:
                print("  You need to enter a number \n")

        if player_choice == 1:
            foe = create_foe(10)
            foe.intro(foe.cid, foe.name, foe.health, foe.attack_power)
            start_battle(foe, player)
        else:
            foe = create_foe(2)
            foe.intro(foe.cid, foe.name, foe.health, foe.attack_power)
            start_battle(foe, player)

            # Reaction Time fight
            print(get_text_info[14])
            time.sleep(1)
            print(get_text_info[15])
            time.sleep(1)
            print(get_text_info[16])
            print()
            time.sleep(random.randint(2, 5))
            print(get_text_info[17])
            start_time = time.time()
            input()
            end_time = time.time()
            reaction_time = end_time - start_time
            print(reaction_time)


def main():
    """
    Main function
    """
    print(Style.RESET_ALL)
    print(Fore.WHITE)
    get_text_info = SHEET.worksheet("text").col_values(2)
    story_intro(get_text_info)

    player = create_player()
    player.name = input("  Enter username: ")
    new_id = int(player.cid) + 1
    add_new_player = [new_id, player.name, 500, 75]
    add_new_player_to_worksheet(add_new_player, "player")

    player.intro(player.cid, player.name, player.health, player.attack_power)

    print(get_text_info[5] + "\n")
    print(get_text_info[6] + "\n")

    # Validate player input choice
    # https://www.youtube.com/watch?v=LUWyA3m_-r0
    # user_response1 = text_info_all.cell(4, 2).value

    decision(1, player)
    decision(2, player)
    decision(3, player)
    print(Style.RESET_ALL)
    exit()


print(Style.RESET_ALL)
main()
