
import abc

class Observer(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def update(self, data):
        pass

class WeatherDisplay(Observer, metaclass=abc.ABCMeta):

    def __init__(self):
        self._temperature = 25
        self._humidity = 50
        self._pressure = 1000

    def update(self, data):
        if "temperature" in data.keys():
            self._temperature = data["temperature"]

        if "humidity" in data.keys():
            self._humidity = data["humidity"]

        if "pressure" in data.keys():
            self._pressure = data["pressure"]

        self.display(self._temperature, self._humidity, self._pressure)

    @abc.abstractmethod
    def display(self, temperature, humidity, pressure):
        pass

class CurrentConditionDisplay(WeatherDisplay):
    def display(self, temperature, humidity, pressure):
        print("Current weather: temperature=[{0}], humidity=[{1}], pressure=[{2}]".format(
            temperature, humidity, pressure))

class StatisticDisplay(WeatherDisplay):

    def __init__(self):
        self._temperature_sum = 0
        self._temperature_total = 0
        self._humidity_sum = 0
        self._humidity_total = 0
        self._pressure_sum = 0
        self._pressure_total = 0

    def display(self, temperature, humidity, pressure):
        self._temperature_sum += temperature
        self._temperature_total += 1
        self._humidity_sum += humidity
        self._humidity_total += 1
        self._pressure_sum += pressure
        self._pressure_total += 1
        print("Statistic weather: temperature=[{0}], humidity=[{1}], pressure=[{2}]".format(
            self._temperature_sum/self._temperature_total,
            self._humidity_sum/self._humidity_total,
            self._pressure_sum/self._pressure_total
            ))

class ForecastDisplay(WeatherDisplay):
    def __init__(self):
        self._temperature_last = 0
        self._humidity_last = 0
        self._pressure_last = 0

    def display(self, temperature, humidity, pressure):

        temperature_diff = temperature - self._temperature_last
        humidity_diff = humidity - self._humidity_last
        pressure_diff = pressure - self._pressure_last

        print("Forecast weather: temperature=[{0}], humidity=[{1}], pressure=[{2}]".format(
            temperature + temperature_diff,
            humidity + humidity_diff,
            pressure + pressure_diff))

        self._temperature_last = temperature
        self._humidity_last = humidity
        self._pressure_last = pressure


