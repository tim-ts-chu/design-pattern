#!/usr/bin/python3

import abc
import subject_module
import observer_module

def print_when_change(weather):
    if weather.is_dirty():
        print("Dirty data: temperature=[{0}], humidity=[{1}], pressure=[{2}]".format(
            weather.get_temperture(),
            weather.get_humidity(),
            weather.get_pressure()))

def main():
    print("Hello, weather world!")

    weather = subject_module.WeatherData()
    current_display = observer_module.CurrentConditionDisplay()
    statistic_display = observer_module.StatisticDisplay()
    forecast_display = observer_module.ForecastDisplay()

    weather.register_observer("current", current_display)
    weather.register_observer("statistic", statistic_display)
    weather.register_observer("forecast", forecast_display)

    for i in range(0, 500):
        print("\n=== Collect [{0}] times ===".format(i))
        # collect and notify can be asynchronous
        weather.collect()
        weather.notify()

    weather.remove_observer("forecast")

    for i in range(500, 1000):
        print("\n=== Collect [{0}] times ===".format(i))
        weather.collect()
        weather.notify()

    # Third party plugin may want to use subject directly
    weather.collect()
    print_when_change(weather)
    weather.reset_dirty()
    print_when_change(weather)
    weather.collect()
    print_when_change(weather)

if __name__ == "__main__":
    main()



