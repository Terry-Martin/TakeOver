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


# Get information from google sheet for player
player_info_all = SHEET.worksheet("player")
player_data = player_info_all.get_all_values()
# player_data = SHEET.get_all_records()
player_id = player_info_all.cell(2, 1).value
player_name = player_info_all.cell(2, 2).value
player_health = int(player_info_all.cell(2, 3).value)
player_attack_power = int(player_info_all.cell(2, 4).value)

# Create player from Character class
player = Character(player_id, player_name, player_health, player_attack_power)

# Get information from google sheet for foe
foe_info_all = SHEET.worksheet("foe")
FOE_TYPE = 9
foe_id = foe_info_all.cell(FOE_TYPE, 1).value
foe_name = foe_info_all.cell(FOE_TYPE, 2).value
foe_health = int(foe_info_all.cell(FOE_TYPE, 3).value)
foe_attack_power = int(foe_info_all.cell(FOE_TYPE, 4).value)

# Create foe from Chatacter class
foe = Character(foe_id, foe_name, foe_health, foe_attack_power)


def start_battle():
    """
    Start battle between player and foe
    """
    while foe.health > 0 and player.health > 0:
        print(f"{player.name} has dealt {player.attack_power} damage")
        foe.health = player.attack(foe.health, player.attack_power)
        print(f"{foe.name} has {foe.health} health remaining\n")
        if foe.health <= 0:
            print(f"{player.name} has defeated the {foe.name}!!!")
            break

        print(f"{foe.name} has dealt {foe.attack_power} damage")
        player.health = foe.attack(player.health, foe.attack_power)
        print(f"{player.name} has {player.health} health remaining\n")
        if player.health <= 0:
            print(f"The {foe.name} has defeated {player.name}!!!")
            break


def add_new_player_to_worksheet(new_player, player_worksheet):
    """
    Add new player to player google sheet
    """
    print(f"Updating {player_worksheet} worksheet...\n")
    player_worksheet_update = SHEET.worksheet(player_worksheet)
    player_worksheet_update.append_row(new_player)
    print(f"{player_worksheet} worksheet updated successfully. \n")


def main():
    """
    Main function
    """
    player.intro(player.cid, player.name, player.health, player.attack_power)
    foe.intro(foe.cid, foe.name, foe.health, foe.attack_power)
    start_battle()
    username = input("Enter username: ")
    print("Username is: " + username)
    add_new_player = [4, username, 500, 75]
    add_new_player_to_worksheet(add_new_player, "player")


main()
