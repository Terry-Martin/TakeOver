"""
Import google sheet
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
    Creat Character class
    """
    def __init__(self, cid, name, health, attack_power):
        self.cid = cid
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, p_name, p_attack_power, p_health, f_name,
               f_attack_power, f_health):
        """
        ATTACK
        """
        while f_health > 0 and p_health > 0:

            print(f"{p_name} has dealt {p_attack_power} damage")
            f_health -= p_attack_power
            print(f"{f_name} has {f_health} health remaining\n")

            if f_health <= 0:
                print(f"{p_name} has defeated the {f_name}!!!")
                break

            print(f"{f_name} has dealt {f_attack_power} damage")
            p_health -= f_attack_power
            print(f"{p_name} has {p_health} health remaining\n")

            if p_health <= 0:
                print(f"The {f_name} has defeated {p_name}!!!")
                break

    def intro(self, cid, name, health, attack_power):
        """
        Display introduction
        """
        print(f"Hi, my name is {name}.")
        print(f"I have the number {cid} tattoed on my arm.")
        print(f"My health is at {health}.")
        print(f"My attack power is {attack_power}.\n")


player_info_all = SHEET.worksheet("player")
# player_data = player_info_all.get_all_values()
player_id = player_info_all.cell(2, 1).value
player_name = player_info_all.cell(2, 2).value
player_health = int(player_info_all.cell(2, 3).value)
player_attack_power = int(player_info_all.cell(2, 4).value)

player = Character(player_id, player_name, player_health, player_attack_power)

player.intro(player.cid, player.name, player.health, player.attack_power)

foe_info_all = SHEET.worksheet("foe")
FOE_TYPE = 5
foe_id = foe_info_all.cell(FOE_TYPE, 1).value
foe_name = foe_info_all.cell(FOE_TYPE, 2).value
foe_health = int(foe_info_all.cell(FOE_TYPE, 3).value)
foe_attack_power = int(foe_info_all.cell(FOE_TYPE, 4).value)

foe = Character(foe_id, foe_name, foe_health, foe_attack_power)

foe.intro(foe.cid, foe.name, foe.health, foe.attack_power)

player.attack(player.name, player.attack_power, player.health, foe.name,
              foe.attack_power, foe.health)
