from character import Character


class Queen(Character):
    def __init__(self):
        super().__init__()

    def fight(self):
        print("Queen does 9 damage")
