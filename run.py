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

        time.sleep(1)
        print(f"  Your name is {name}.")
        print(f"  {cid}Your current health is {health}.")
        print(f"  Your attack power is {attack_power}.\n")
        time.sleep(1)


def create_player(new_name):
    """
    Create player
    """

    # Get current information from google sheet for player
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

    # Get information from google sheet for which ever foe number is passed in
    get_foe_info = SHEET.worksheet("foe").row_values(foe_number)
    foe_id = get_foe_info[0]
    foe_name = get_foe_info[1]
    foe_health = int(get_foe_info[2])
    foe_attack_power = int(get_foe_info[3])

    # Create foe from Chatacter class and send back to main function
    return Character(foe_id, foe_name, foe_health, foe_attack_power)


def game_over():
    """
    End game display
    """

    # Format text
    result = pyfiglet.figlet_format("              GAME OVER")
    print(Fore.WHITE)
    print(Back.RED)
    print(result)
    print(Style.RESET_ALL)
    print(Fore.WHITE)
    time.sleep(3)

    # Restart app
    print("Restarting game.....")
    time.sleep(4)
    main()


def start_battle(foe, player):
    """
    Start battle between player and foe
    """

    # Loop through until either player or foe is defeated
    while foe.health > 0 and player.health > 0:
        # Display damage taken for each attack and remaining health points
        print(Fore.RED + f"  {player.name} has dealt {player.attack_power}" +
              " damage")
        print(Fore.WHITE)
        foe.health = player.attack(foe.health, player.attack_power)
        print(f"  {foe.name} has {foe.health} health remaining\n")
        if foe.health <= 0:
            print(f"  {player.name} has defeated the {foe.name}!!! \n")
            time.sleep(2)
            # Foe defeated and break loop
            # If there is another foe in this battle, it will start next
            break

        # Display damage taken for each attack and remaining health points
        print(f"  {foe.name} has dealt {foe.attack_power} damage")
        player.health = foe.attack(player.health, foe.attack_power)
        print(Fore.GREEN + f"  {player.name} has {player.health}" +
              " health remaining\n")
        print(Fore.WHITE)
        if player.health <= 0:
            print(f"  The {foe.name} has defeated {player.name}!!! \n")
            time.sleep(2)
            # Player defeated and game over
            game_over()


def story_intro(story_start):
    """
    Display story start
    """

    # https://pypi.org/project/colorama/
    # Format text
    result = pyfiglet.figlet_format("              TakeOver")
    print(Back.BLUE)
    print(Style.BRIGHT)
    print(result)
    print(Style.RESET_ALL)
    print(Fore.WHITE)

    # Time delay idea from classmate Darragh Lynch
    time.sleep(1)
    # Display story intro
    # Text pulled from "text" google sheet
    print("\n" + story_start[1] + "\n")
    time.sleep(2)
    print(story_start[2] + "\n")
    time.sleep(2)
    print(story_start[3] + "\n")
    time.sleep(2)
    print(story_start[4] + "\n")


def decision(decision_tree, player):
    """
    Captures which branch/decision tree the player is currently at
    """
    # Text pulled from "text" google sheet
    get_text_info = SHEET.worksheet("text").col_values(2)

    # First decision tree for player to make selection
    if decision_tree == 1:
        while True:
            player_choice = input(get_text_info[7])
            # Validate user entering a number
            try:
                player_choice = int(player_choice)
                break
            except ValueError:
                print("  You need to enter a number" + "\n")

        if player_choice == 1:
            # Battle will have 3 foes

            # Create first foe
            foe = create_foe(3)
            # Display info on first foe
            foe.intro(foe.cid, foe.name, foe.health, foe.attack_power)
            # Begin battle between first foe and player
            start_battle(foe, player)

            # Begin battle with second foe
            foe_two = create_foe(3)
            foe_two.intro(foe_two.cid, foe_two.name, foe_two.health,
                          foe_two.attack_power)
            start_battle(foe_two, player)

            foe_three = create_foe(4)
            foe_three.intro(foe_three.cid, foe_three.name, foe_three.health,
                            foe_three.attack_power)
            start_battle(foe_three, player)
        else:
            # Battle will have 3 foes
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
        time.sleep(1)
        print("\n" + get_text_info[8] + "\n")
        time.sleep(1)
        print(get_text_info[9] + "\n")
        time.sleep(1)

    # Second decision tree for player to make selection
    elif decision_tree == 2:
        # Validate user entering a number
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
        time.sleep(1)
        print("\n" + get_text_info[11] + "\n")
        time.sleep(1)
        print(get_text_info[12] + "\n")
        time.sleep(1)

    # Third decision tree for player to make selection
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
            # User hits enter when GO word is diplayed. Reaction time is noted
            print(get_text_info[14])
            time.sleep(1)
            print(get_text_info[15])
            time.sleep(1)
            print(get_text_info[16])
            print()
            # Randon time for the word GO to appear between 2 and 5 seconds
            time.sleep(random.randint(2, 5))
            print(get_text_info[17])
            start_time = time.time()
            input()
            end_time = time.time()
            # Player reaction time check against foe time
            player_reaction_time = end_time - start_time
            foe_reaction_time = 0.4
            time.sleep(1)
            # Display player and foe reaction times
            print(f"Your reaction time was {player_reaction_time}")
            print(f"{foe.name} reaction time was {foe_reaction_time}")
            time.sleep(1)

            # Foe defeated if player reaction time is faster
            if player_reaction_time <= foe_reaction_time:
                print(f"You take out the {foe.name} with one clean hit")
                foe.health = 0
                print(Fore.GREEN + f"  {player.name} has {player.health}" +
                      " health remaining\n")
                time.sleep(1)
            # Player takes 200 damage if foe reaction time is faster
            else:
                print(f"{foe.name} gets in a quick attack")
                player.health = player.health - 200
                print(Fore.GREEN + f"  {player.name} has {player.health}" +
                      " health remaining\n")
                time.sleep(1)
                if player.health <= 0:
                    game_over()


def boss_battle():
    """
    Final battle
    """

    time.sleep(1)
    get_text_info = SHEET.worksheet("text").col_values(2)
    print(get_text_info[18] + "\n")
    time.sleep(1)


def main():
    """
    Main function to start game
    """

    # Format text and display
    print(Style.RESET_ALL)
    print(Fore.WHITE)
    get_text_info = SHEET.worksheet("text").col_values(2)
    story_intro(get_text_info)

    # Prompt for user
    enter_name = input("  Enter username: ")

    # create new played from character class based on inputted username
    player = create_player(enter_name)
    print()

    time.sleep(1)
    print(get_text_info[5] + "\n")
    time.sleep(1)
    print(get_text_info[6] + "\n")

    # https://www.youtube.com/watch?v=LUWyA3m_-r0

    decision(1, player)
    decision(2, player)
    decision(3, player)
    boss_battle()
    print(Style.RESET_ALL)
    main()


main()
