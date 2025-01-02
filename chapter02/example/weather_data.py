from subject import Subject


class WeatherData(Subject):
    def __init__(self):
        self.__observers = []
        self.__temperature = None
        self.__humidity = None
        self.__pressure = None

    def register_observer(self, observer):
        self.__observers.append(observer)

    def remove_observer(self, observer):
        self.__observers.remove(observer)

    def notify_observers(self):
        for observer in self.__observers:
            observer.update(self.__temperature,
                            self.__humidity, self.__pressure)

    def measurements_changed(self):
        self.notify_observers()

    def set_measurements(self, temperature, humidity, pressure):
        self.__temperature = temperature
        self.__humidity = humidity
        self.__pressure = pressure
        self.measurements_changed()
