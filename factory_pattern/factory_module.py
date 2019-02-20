
import abc

class Dough(metaclass=abc.ABCMeta):
    def show(self):
        return self.__class__.__name__
class ThickDough(Dough):
    pass
class ThinDough(Dough):
    pass
class Sauce(metaclass=abc.ABCMeta):
    def show(self):
        return self.__class__.__name__
class HeavySauce(Sauce):
    pass
class LightSauce(Sauce):
    pass

# This class is so called abstract factory
class IngredientFactory(metaclass=abc.ABCMeta):
    # similar to the factory method
    @abc.abstractmethod
    def createDought(self):
        pass

    # similar to the factory method
    @abc.abstractmethod
    def createSauce(self):
        pass

# provide different factory for different product family
class NYIngredientFactory(IngredientFactory):
    def createDought(self):
        return ThickDough()
    def createSauce(self):
        return HeavySauce()

class ChicagoIngredientFactory(IngredientFactory):
    def createDought(self):
        return ThinDough()
    def createSauce(self):
        return LightSauce()

# general class of products
class Pizza(metaclass=abc.ABCMeta):

    def __init__(self, ingredient_factory):
        self._factory = ingredient_factory
        self._dough = None
        self._sauce = None

    def prepare(self):
        self._dough = self._factory.createDought()
        self._sauce = self._factory.createSauce()

    def bake(self):
        print('pizza is baking...')
    def cut(self):
        print('pizza is cutting...')
    def box(self):
        print('pizza is boxing...')
    def show(self):
        return self._dough.show() + ' ' + self._sauce.show() + ' ' + self.__class__.__name__

class NYCheesePizza(Pizza):
    pass
class NYClam(Pizza):
    pass
class NYVeggiePizza(Pizza):
    pass
class ChicagoCheesePizza(Pizza):
    pass
class ChicagoClamPizza(Pizza):
    pass
class ChicagoVeggiePizza(Pizza):
    pass

# user client
class PizzaStore(metaclass=abc.ABCMeta):
    # This method is so called factory method
    @abc.abstractmethod
    def createPizza(self, flavor):
        pass

    def orderPizza(self, flavor):
        pizza = self.createPizza(flavor)
        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()
        return pizza

class NYPizzaStore(PizzaStore):
    # factory mehtod implementation
    def createPizza(self, flavor):
        factory = NYIngredientFactory()
        pizza = None
        if flavor == 'Cheese':
            pizza = NYCheesePizza(factory)
        elif flavor == 'Clam':
            pizza = NYClamPizza(factory)
        else:
            pizza = NYVeggiePizza(factory)
        return pizza

class ChicagoPizzaStore(PizzaStore):
    # factory mehtod implementation
    def createPizza(self, flavor):
        factory = ChicagoIngredientFactory()
        pizza = None
        if flavor == 'Cheese':
            pizza = ChicagoChesePizza(factory)
        elif flavor == 'Clam':
            pizza = ChicagoClamPizza(factory)
        else:
            pizza = ChicagoVeggiePizza(factory)
        return pizza


