from display_element import DisplayElement
from observer import Observer
from weather_data import WeatherData


class ForecastDisplay(Observer, DisplayElement):
    def __init__(self, weather_data: WeatherData):
        super().__init__()
        self.__current_pressure = 29.92
        self.__last_pressure = None
        self.__weather_data = weather_data
        weather_data.register_observer(self)

    def display(self):
        print(f"Forecasted pressure: {self.__current_pressure}")

    def update(self):
        self.__last_pressure = self.__current_pressure
        self.__current_pressure = self.__weather_data.get_pressure()
        self.display()
