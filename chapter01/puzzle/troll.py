from character import Character


class Troll(Character):
    def __init__(self):
        super().__init__()

    def fight(self):
        print("Troll does 4 damage")
