
import abc

class Beverage(metaclass=abc.ABCMeta):
    _description = 'Unknown beverage'
    _cost = 0
    def getDescription(self):
        return self._description

    def cost(self):
        return self._cost

class HouseBlend(Beverage):
    _description = 'HouseBlend'
    _cost = 0.89

class DarkRoast(Beverage):
    _description = 'DarkRoast'
    _cost = 0.99

class Espresso(Beverage):
    _description = 'Espresso'
    _cost = 1.99

class Decaf(Beverage):
    _description = 'Decaf'
    _cost = 1.05

# Here we use decorating class because of the advantage of inheritance
# The another way is using decorating function
class CondimentDecorator(metaclass=abc.ABCMeta):
    _description = 'Unknown Condiment'
    _cost = 0
    def __init__(self, decorator_target):
        self.target = decorator_target

    def __call__(self, f):
        def wrapped_f(*args):
            if self.target == 'cost':
                return self._cost + f(*args)
            else:
                return self._description + ' ' + f(*args)
        return wrapped_f


class Mocha(CondimentDecorator):
    _description = 'Mocha'
    _cost = 0.2

class Milk(CondimentDecorator):
    _description = 'Milk'
    _cost = 0.25

class Soy(CondimentDecorator):
    _description = 'Soy'
    _cost = 0.15

class Whip(CondimentDecorator):
    _description = 'Whip'
    _cost = 0.1









