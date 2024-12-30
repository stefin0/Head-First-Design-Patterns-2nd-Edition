from abc import ABC, abstractmethod


class Duck(ABC):
    def __init__(self):
        self.fly_behavior = None
        self.quack_behavior = None

    @abstractmethod
    def display(self):
        pass

    def set_fly_behavior(self, fly_behavior):
        self.fly_behavior = fly_behavior

    def set_quack_behavior(self, quack_behavior):
        self.quack_behavior = quack_behavior

    def perform_fly(self):
        self.fly_behavior.fly()

    def perform_quack(self):
        self.quack_behavior.quack()

    def swim(self):
        print("All ducks float, even decoys!")
