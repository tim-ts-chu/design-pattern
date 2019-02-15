
import abc

class FlyBehavior(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def fly(self):
        pass

class FlyWithWings(FlyBehavior):
    def fly(self):
        print("I'm fly with wings")

class FlyNoWay(FlyBehavior):
    def fly(self):
        print("I cannot fly")

class QuackBehavior(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def quack(self):
        pass

class Quack(QuackBehavior):
    def quack(self):
        print("I'm quacking")

class Squeak(QuackBehavior):
    def quack(self):
        print("I'm squeaking")

class MuteQuack(QuackBehavior):
    def quack(self):
        print("I'm mute")

