from abc import ABC, abstractmethod


class Character(ABC):
    def __init__(self):
        self.weapon_behavior = None

    @abstractmethod
    def fight(self):
        pass

    def set_weapon(self, weapon_behavior):
        self.weapon_behavior = weapon_behavior
