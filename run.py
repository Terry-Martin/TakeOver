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
DELAY_1 = 1
DELAY_2 = 2
DELAY_3 = 3
DELAY_4 = 4


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
        time.sleep(DELAY_1)
        print(f"  Your name is {name}.")
        print(f"  {cid}Your current health is {health}.")
        print(f"  Your attack power is {attack_power}.\n")
        time.sleep(DELAY_1)


def create_player(new_name):
    """
    Create player
    """
    # Get information from google sheet for player

    get_player_info = SHEET.worksheet("player").col_values(1)

    # Get new id number which is 1 higher than previous id number
    player_id = len(get_player_info)
    player_name = new_name
    player_health = 500
    player_attack_power = 75

    # Add new player details to sheet
    SHEET.worksheet("player").append_row([player_id, player_name,
                                         player_health, player_attack_power])

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


def game_over():
    """
    Format game over text
    """
    result = pyfiglet.figlet_format("              GAME OVER")
    print(Back.RED)
    print(result)
    print(Style.RESET_ALL)
    print(Fore.WHITE)
    time.sleep(DELAY_3)
    print("Restarting game.....")
    time.sleep(DELAY_3)
    main()


def start_battle(foe, player):
    """
    Start battle between player and foe
    """
    while foe.health > 0 and player.health > 0:

        print(Fore.RED + f"  {player.name} has dealt {player.attack_power}" +
              " damage")
        print(Fore.WHITE)
        foe.health = player.attack(foe.health, player.attack_power)
        print(f"  {foe.name} has {foe.health} health remaining\n")
        if foe.health <= 0:
            print(f"  {player.name} has defeated the {foe.name}!!! \n")
            time.sleep(DELAY_2)
            break

        print(f"  {foe.name} has dealt {foe.attack_power} damage")
        player.health = foe.attack(player.health, foe.attack_power)
        print(Fore.GREEN + f"  {player.name} has {player.health}" +
              " health remaining\n")
        print(Fore.WHITE)
        if player.health <= 0:
            print(f"  The {foe.name} has defeated {player.name}!!! \n")
            time.sleep(DELAY_1)
            game_over()


def story_intro(story_start):
    """
    Display story start
    """
    # https://pypi.org/project/colorama/
    result = pyfiglet.figlet_format("              TakeOver")
    print(Back.BLUE)
    print(Style.BRIGHT)
    print(result)
    print(Style.RESET_ALL)
    print(Fore.WHITE)

    # print(Back.GREEN + 'and with a green background')
    # print(Style.DIM + 'and in dim text')
    # print(Style.RESET_ALL)
    # print(Style.BRIGHT + 'and in bright text')
    # print(Style.RESET_ALL)
    # print(Back.BLUE)

    # Time delay idea from classmate Darragh Lynch
    time.sleep(DELAY_1)
    print("\n" + story_start[1] + "\n")
    time.sleep(DELAY_2)
    print(story_start[2] + "\n")
    time.sleep(DELAY_2)
    print(story_start[3] + "\n")
    time.sleep(DELAY_2)
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
        time.sleep(DELAY_1)
        print("\n" + get_text_info[8] + "\n")
        time.sleep(DELAY_1)
        print(get_text_info[9] + "\n")
        time.sleep(DELAY_1)

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
        time.sleep(DELAY_1)
        print("\n" + get_text_info[11] + "\n")
        time.sleep(DELAY_1)
        print(get_text_info[12] + "\n")
        time.sleep(DELAY_1)

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
            foe = create_foe(11)
            foe.intro(foe.cid, foe.name, foe.health, foe.attack_power)

            # Reaction Time fight
            print(get_text_info[14])
            time.sleep(DELAY_1)
            print(get_text_info[15])
            time.sleep(DELAY_1)
            print(get_text_info[16])
            print()
            time.sleep(random.randint(2, 5))
            print(get_text_info[17])
            start_time = time.time()
            input()
            end_time = time.time()
            player_reaction_time = end_time - start_time
            foe_reaction_time = 0.4
            time.sleep(DELAY_1)
            print(f"Your reaction time was {player_reaction_time}")
            print(f"{foe.name} reaction time was {foe_reaction_time}")
            time.sleep(DELAY_1)

            if player_reaction_time <= foe_reaction_time:
                print(f"You take out the {foe.name} with one clean hit")
                foe.health = 0
                print(Fore.GREEN + f"  {player.name} has {player.health}" +
                      " health remaining\n")
                time.sleep(DELAY_1)
            else:
                print(f"{foe.name} gets in a quick attack")
                player.health = player.health - 200
                print(Fore.GREEN + f"  {player.name} has {player.health}" +
                      " health remaining\n")
                time.sleep(DELAY_1)
                if player.health <= 0:
                    game_over()


def boss_battle():
    """
    Final battle
    """
    time.sleep(DELAY_1)
    get_text_info = SHEET.worksheet("text").col_values(2)
    print(get_text_info[18] + "\n")
    time.sleep(DELAY_1)


def main():
    """
    Main function
    """
    print(Style.RESET_ALL)
    print(Fore.WHITE)
    get_text_info = SHEET.worksheet("text").col_values(2)
    story_intro(get_text_info)

    enter_name = input("  Enter username: ")

    # create new played from character class
    player = create_player(enter_name)
    print()

    time.sleep(DELAY_1)
    print(get_text_info[5] + "\n")
    time.sleep(DELAY_1)
    print(get_text_info[6] + "\n")

    # Validate player input choice
    # https://www.youtube.com/watch?v=LUWyA3m_-r0
    # user_response1 = text_info_all.cell(4, 2).value

    decision(1, player)
    decision(2, player)
    decision(3, player)
    boss_battle()
    print(Style.RESET_ALL)
    # exit()
    main()


main()
