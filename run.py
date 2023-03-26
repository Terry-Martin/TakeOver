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

foe = SHEET.worksheet("foe")
foe_data = foe.get_all_values()
foe_name = foe.col_values(2)
print(foe_data)
print(foe_name)

player = SHEET.worksheet("player")
player_data = player.get_all_values()
print(player_data)

value = foe.cell(4, 4)

class Character:
    """
    Creat Character class
    """
    def __init__(self, cid, name, health, attack):
        self.cid = cid
        self.name = name
        self.health = health
        self.attack = attack


foes = Character(101, foe_name, 500, value)
print(foes.attack)
