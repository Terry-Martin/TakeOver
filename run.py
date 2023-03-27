"""
Import google sheet
"""
import gspread
from google.oauth2.service_account import Credentials
# import Character

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

    def attack(self, name, attack_power):
        """
        ATTACK
        """
        damage_dealt = attack_power
        print(f"{name} has dealt {damage_dealt} damage")


player_info_all = SHEET.worksheet("player")
# player_data = player_info_all.get_all_values()
player_id = player_info_all.cell(2, 1).value
player_name = player_info_all.cell(2, 2).value
player_health = int(player_info_all.cell(2, 3).value)
player_attack_power = int(player_info_all.cell(2, 4).value)

player = Character(player_id, player_name, player_health, player_attack_power)
print(f"Hi, my name is {player.name}.")
print(f"I have {player.cid} tattoed on my arm.")
print(f"My health is at {player.health}.")
print(f"My attack power is {player.attack_power}.\n")

foe_info_all = SHEET.worksheet("foe")
# foe_data = foe.get_all_values()
foe_id = foe_info_all.cell(2, 1).value
foe_name = foe_info_all.cell(2, 2).value
foe_health = int(foe_info_all.cell(2, 3).value)
foe_attack_power = int(foe_info_all.cell(2, 4).value)

foe = Character(foe_id, foe_name, foe_health, foe_attack_power)
print(f"Hi, my name is {foe.name}.")
print(f"I have {foe.cid} tattoed on my arm.")
print(f"My health is at {foe.health}.")
print(f"My attack power is {foe.attack_power}.\n")

while foe.health > 0:
    player.attack(player.name, player.attack_power)
    foe.health -= player.attack_power
    print(f"{foe.name} has {foe.health} health\n")

while player.health > 0:
    foe.attack(foe.name, foe.attack_power)
    player.health -= foe.attack_power
    print(f"{player.name} has {player.health} health remaining\n")
