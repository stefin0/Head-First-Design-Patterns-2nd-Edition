from chapter03.example.beverage import Beverage
from chapter03.example.condiment_decorator import CondimentDecorator


class Mocha(CondimentDecorator):
    def __init__(self, beverage: Beverage):
        super().__init__(beverage)

    def get_description(self) -> str:
        return self.beverage.get_description() + ", Mocha"

    def cost(self) -> float:
        return self.beverage.cost() + 0.20
