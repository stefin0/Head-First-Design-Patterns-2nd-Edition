from observer import Observer
from display_element import DisplayElement
from weather_data import WeatherData


class CurrentConditionsDisplay(Observer, DisplayElement):
    def __init__(self, weather_data: WeatherData):
        super().__init__()
        self.__temperature = None
        self.__humidity = None
        self.__weather_data = weather_data
        weather_data.register_observer(self)

    def update(self):
        self.__temperature = self.__weather_data.get_temperature()
        self.__humidity = self.__weather_data.get_humidity()
        self.display()

    def display(self):
        print(f"Current conditions: {self.__temperature}F degrees and {
              self.__humidity}% humidity")
