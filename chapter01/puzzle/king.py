from character import Character


class King(Character):
    def __init__(self):
        super().__init__()

    def fight(self):
        print("King does 10 damage")
