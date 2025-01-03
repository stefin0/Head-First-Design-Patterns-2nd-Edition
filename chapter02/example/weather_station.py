from weather_data import WeatherData
from current_conditions_display import CurrentConditionsDisplay
from forecast_display import ForecastDisplay


if __name__ == "__main__":
    weather_data = WeatherData()
    current_display = CurrentConditionsDisplay(weather_data)
    forecast_display = ForecastDisplay(weather_data)

    weather_data.set_measurements(80, 65, 30.4)
    weather_data.set_measurements(82, 70, 29.2)
