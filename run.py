"""
Import google sheet
Import adapted from LoveSandwiches example
"""
import gspread
from google.oauth2.service_account import Credentials

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
        print(f"My name is {name}.")
        print(f"The number {cid} is tattoed on my arm.")
        print(f"My health is {health}.")
        print(f"My attack power is {attack_power}.\n")


def create_player():
    """
    Create player
    """
    # Get information from google sheet for player
    player_info_all = SHEET.worksheet("player")
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
    foe_info_all = SHEET.worksheet("foe")
    foe_id = foe_info_all.cell(foe_number, 1).value
    foe_name = foe_info_all.cell(foe_number, 2).value
    foe_health = int(foe_info_all.cell(foe_number, 3).value)
    foe_attack_power = int(foe_info_all.cell(foe_number, 4).value)

    # Create foe from Chatacter class and send back to main function
    return Character(foe_id, foe_name, foe_health, foe_attack_power)


def start_battle(foe, player):
    """
    Start battle between player and foe
    """
    while foe.health > 0 and player.health > 0:
        print(f"{player.name} has dealt {player.attack_power} damage")
        foe.health = player.attack(foe.health, player.attack_power)
        print(f"{foe.name} has {foe.health} health remaining\n")
        if foe.health <= 0:
            print(f"{player.name} has defeated the {foe.name}!!! \n")
            break

        print(f"{foe.name} has dealt {foe.attack_power} damage")
        player.health = foe.attack(player.health, foe.attack_power)
        print(f"{player.name} has {player.health} health remaining\n")
        if player.health <= 0:
            print(f"The {foe.name} has defeated {player.name}!!! \n")
            break


def add_new_player_to_worksheet(new_player, player_worksheet):
    """
    Add new player to player google sheet
    """
    player_worksheet_update = SHEET.worksheet(player_worksheet)
    player_worksheet_update.append_row(new_player)


def main():
    """
    Main function
    """
    player = create_player()
    player.name = input("Enter username: \n")
    new_id = int(player.cid) + 1
    add_new_player = [new_id, player.name, 500, 75]
    add_new_player_to_worksheet(add_new_player, "player")

    player.intro(player.cid, player.name, player.health, player.attack_power)

    print("\nYou see a camp on the road.\n")
    print("Do you wish to approach it or keep riding towards town?\n")
    # Validate player input choice
    # https://www.youtube.com/watch?v=LUWyA3m_-r0
    while True:
        player_choice = input("Press 1 to apprach camp or 2 to pass it by\n")

        try:
            player_choice = int(player_choice)
            break
        except ValueError:
            print("You need to enter a number")
            print()

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

    print("\nThe guard stops you at the gate and demand you remove your weapon. \n")
    print("Do you wish to approach the guard or solider on horseback? \n")
    # Validate player input choice
    while True:
        player_choice = input("Press 1 to attack guard or 2 to apprach soldier \n")

        try:
            player_choice = int(player_choice)
            break
        except ValueError:
            print("You need to enter a number")
            print()

    if player_choice == 1:
        foe = create_foe(4)
    else:
        foe = create_foe(5)

    player.intro(player.cid, player.name, player.health, player.attack_power)
    foe.intro(foe.cid, foe.name, foe.health, foe.attack_power)

    start_battle(foe, player)


main()
