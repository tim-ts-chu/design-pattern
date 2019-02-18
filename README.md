# Design Pattern
Exercises of design pattern in Python

## Table of Content

* [Strategy Pattern](#strategy-pattern)
* [Oberver Pattern](observer_pattern/README.md)
* Decorator Pattern
* Factory Pattern
* [Singleton Pattern](singleton_pattern/README.md)

## Strategy Pattern
-------------------
### Definition
Strategy pattern is that we try to find out the changed parts, and encapsulate it. This pattern make the core algorithms be alternated easily without effecting the current program which is not related with changed parts.

### Rules
1. Encapsulate changed parts
2. Use composition more, inheritance less
3. Write program based on interface instead of implementation

### Example
A duck example:
Here we design a duck abstract class with two kinds of abilities (algorithm), that are flying and quacking. Leter, due to flying and quacking behavior are different for different types of duck, we encapsulate both two functionality into two separately class for easily changing.
![Duck example diagram](strategy_pattern/strategy_pattern.png)

### Applications
* neuron network -> activation function
* read/write -> compression algorithm

## Observer Pattern
-------------------
### Definition
Observer pattern is that when we have one writer and many readers, then we can use observer pattern to realize it.

### Rules
1. Encapsulate changed parts
2. Use composition more, inheritance less
3. Write program based on interface instead of implementation
4. **Loosen the coupling between objects**

## Example
A weather example:
There is an subject in the example named weather. The subject is responsible for getting the weather data from other class and maintaining the registration of observers. There could be many observers for different purpose, but all of them have to register to subject in order to receive the updated weather data.
![Weather diagram](observer_pattern/observer_pattern.png)

### Applications
* task progress
* event driven pattern -> if one event comes, subject broadcast to all listeners.

## Decorator Pattern
### Definition
### Rules
### Example
### Applications

## Factory Pattern
### Definition
### Rules
### Example
### Applications

## Singleton Pattern
--------------------
### Definition
Singleton pattern is that we only have a unique instance for a class in a runtime.

### Rules

### Example
A singleton example:
The example is quite simple. We only implement a singleton class and make sure that all instances coming from the singleton class are actually the same instance.
![Singleton diagram](singleton_pattern/singleton_pattern.png)

### Applications
* Global variable/function/flag
* Single handler
* Request sender (avoid to login everytime)



