from abc import ABC, abstractmethod


class WeaponBehavior(ABC):
    @abstractmethod
    def use_weapon(self):
        pass
