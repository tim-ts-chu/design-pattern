
import abc
import random
import observer_module 

class Subject(metaclass=abc.ABCMeta):
    
    def __init__(self):
        self._observers = {}

    def register_observer(self, key, observer):
        if not isinstance(observer, observer_module.Observer):
            raise TypeError("Input is not an observer")

        if key in self._observers.keys():
            raise KeyError("This key has already register")

        self._observers[key] = observer

    def remove_observer(self, key):
        if key not in self._observers.keys():
            raise KeyError("key [{0}] not found".format(key))

        del self._observers[key]

    def notify_observers(self, data):
        for key, observer in self._observers.items():
            observer.update(data)

class WeatherData(Subject):

    def __init__(self):
        super(WeatherData, self).__init__()
        self._temperature = 25
        self._humidity = 50
        self._pressure = 1000
        self._dirty = False

    def collect(self):
        self._temperature = 25 + random.randint(-10, 10)
        self._humidity = 50 + random.randint(-30, 30)
        self._pressure = 1000 + random.randint(-100, 100)
        self._dirty = True

    def notify(self):

        data = {
                "temperature": self._temperature,
                "humidity": self._humidity,
                "pressure": self._pressure
                }
        self.notify_observers(data)

    def get_temperture(self):
        return self._temperature

    def get_humidity(self):
        return self._humidity

    def get_pressure(self):
        return self._pressure

    def is_dirty(self):
        return self._dirty

    def reset_dirty(self):
        self._dirty = False


