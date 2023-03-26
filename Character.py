class Character:
    """
    Creat Character class
    """
    def __init__(self, cid, name, health, attack):
        self.cid = cid
        self.name = name
        self.health = health
        self.attack = attack


foe = Character(101, 'Ralf', 500, 230)
