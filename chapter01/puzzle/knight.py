from character import Character


class Knight(Character):
    def __init__(self):
        super().__init__()

    def fight(self):
        print("Knight does 20 damage")
