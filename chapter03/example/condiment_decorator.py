from abc import abstractmethod
from chapter03.example.beverage import Beverage


class CondimentDecorator(Beverage):
    def __init__(self, beverage: Beverage):
        super().__init__()
        self.beverage = beverage

    @abstractmethod
    def get_description(self) -> str:
        pass
