from observer import Observer
from display_element import DisplayElement


class CurrentConditionsDisplay(Observer, DisplayElement):
    def __init__(self, weather_data):
        self.__temperature = None
        self.__humidity = None
        self.__weather_data = weather_data
        weather_data.register_observer(self)

    def update(self, temperature, humidity, pressure):
        self.__temperature = temperature
        self.__humidity = humidity
        self.display()

    def display(self):
        print(f"Current conditions: {self.__temperature}F degrees and {
              self.__humidity}% humidity")
