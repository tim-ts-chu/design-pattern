
import abc
import behavior_module

class Duck(metaclass=abc.ABCMeta):

    def __init__(self):
        self._fly_behavior = None
        self._quack_behavior = None

    def _check_behavior(self):
        if not self._fly_behavior:
            raise AttributeError("The fly behavior is not set.")

        if not self._quack_behavior:
            raise AttributeError("The quack behavior is not set.")

    @property
    def fly_behavior(self):
        raise AttributeError("This is private attribute.")

    @property
    def quack_behavior(self):
        raise AttributeError("This is private attribute.")


    @abc.abstractmethod
    def display(self):
        pass

    @fly_behavior.setter
    def fly_behavior(self, fly_behavior):
        if isinstance(fly_behavior, behavior_module.FlyBehavior):
            self._fly_behavior = fly_behavior
        else:
            raise TypeError("The agruement is not instance of FlyBehavior.")

    @quack_behavior.setter
    def quack_behavior(self, quack_behavior):
        if isinstance(quack_behavior, behavior_module.QuackBehavior):
            self._quack_behavior = quack_behavior
        else:
            raise TypeError("The agruement is not instance of QuackBehavior.")

    def swim(self):
        print("I'm swimming")

    def performFly(self):
        self._check_behavior()
        self._fly_behavior.fly()

    def performQuack(self):
        self._check_behavior()
        self._quack_behavior.quack()

class MallardDuck(Duck):
    def display(self):
        print("I'm a mallard duck");

class RubberDuck(Duck):
    def display(self):
        print("I'm a rubber duck");

class RedheadDuck(Duck):
    def display(self):
        print("I'm a redhead duck");

class DecoyDuck(Duck):
    def display(self):
        print("I'm a decoy duck");

