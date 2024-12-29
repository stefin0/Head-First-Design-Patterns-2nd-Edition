from duck import Duck
from quack import Quack
from fly_with_wings import FlyWithWings


class MallardDuck(Duck):
    def __init__(self):
        super().__init__()
        self.quack_behavior = Quack()
        self.fly_behavior = FlyWithWings()

    def display(self):
        print("I'm a real Mallard duck")
