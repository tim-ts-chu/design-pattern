
import abc

class PizzaStore(abc.ABC):
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
        pizza = None
        if flavor == 'Cheese':
            pizza = NYChesePizza()
        elif flavor == 'Clam':
            pizza = NYClamPizza()
        else:
            pizza = NYVeggiePizza()
        return pizza

class ChicagoPizzaStore(PizzaStore):
    # factory mehtod implementation
    def createPizza(self, flavor):
        pizza = None
        if flavor == 'Cheese':
            pizza = ChicagoChesePizza()
        elif flavor == 'Clam':
            pizza = ChicagoClamPizza()
        else:
            pizza = ChicagoVeggiePizza()
        return pizza

class Pizza(abc.ABC):
    @abc.abstractmethod
    def prepare(self):
        pass
    def bake(self):
        print('pizza is baking...')
    def cut(self):
        print('pizza is cutting...')
    def box(self):
        print('pizza is boxing...')
    def show(self):
        return self.__class__.__name__

class NYCheesePizza(Pizza):
    def prepare(self):
        print('prepared a NY Cheeese flavor pizza')
class NYClam(Pizza):
    def prepare(self):
        print('prepared a NY Clam flavor pizza')
class NYVeggiePizza(Pizza):
    def prepare(self):
        print('prepared a NY Veggie flavor pizza')
class ChicagoCheesePizza(Pizza):
    def prepare(self):
        print('prepared a Chicago Cheeese flavor pizza')
class ChicagoClamPizza(Pizza):
    def prepare(self):
        print('prepared a Chicago Clam flavor pizza')
class ChicagoVeggiePizza(Pizza):
    def prepare(self):
        print('prepared a Chicago Veggie flavor pizza')

