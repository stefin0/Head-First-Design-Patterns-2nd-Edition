from abc import ABC, abstractmethod


class DisplayElement(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def display(self):
        pass
