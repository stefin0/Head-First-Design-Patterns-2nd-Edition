from duck import Duck
from fly_no_way import FlyNoWay
from quack import Quack


class ModelDuck(Duck):
    def __init__(self):
        super().__init__()
        self.fly_behavior = FlyNoWay()
        self.quack_behavior = Quack()

    def display(self):
        print("I'm a model duck")