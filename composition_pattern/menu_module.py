
import abc

class MenuComponent(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def __init__(self):
        self.name = None
        self.price = None
        self.children = []

    @abc.abstractmethod
    def add(self, child):
        pass

    @abc.abstractmethod
    def remove(self, idx):
        pass

    @abc.abstractmethod
    def show(self):
        pass

    def traverse(self, func_name):
        try:
            func = getattr(self, func_name)
            func()
        except AttributeError:
            print('function: {} not found'.format(func_name))

        for child in self.children:
            child.traverse(func_name)

class Menu(MenuComponent):
    def __init__(self, name):
        self.name = name
        self.price = None
        self.children = []
    def add(self, child):
        self.children.append(child)
    def remove(self, idx):
        if idx > len(self.children) - 1:
            raise IndexError
        del self.children[idx]
    def show(self):
        print('=== {} Menu ==='.format(self.name))

class MenuItem(MenuComponent):
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.children = []
    def add(self, child):
        raise NotImplementedError
    def remove(self, idx):
        raise NotImplementedError
    def show(self):
        print('{}: {}'.format(self.name, self.price))


pancake_menu = Menu('PanCake')
item = MenuItem('Regular Pancake', 2.99)
pancake_menu.add(item)
item = MenuItem('Chese Pancake', 3.50)
pancake_menu.add(item)
item = MenuItem('Bacon Pancake', 3.99)
pancake_menu.add(item)

dessert_menu = Menu('Dessert')
item = MenuItem('Ice Cream', 1.99)
dessert_menu.add(item)
item = MenuItem('Chocolate Cookie', 0.99)
dessert_menu.add(item)
item = MenuItem('Mango Shake', 2.99)
dessert_menu.add(item)

diner_menu = Menu('Diner')
item = MenuItem('Pasta', 2.99)
diner_menu.add(item)
item = MenuItem('Pizza', 4.99)
diner_menu.add(item)
item = MenuItem('Hamburger', 3.49)
diner_menu.add(item)
diner_menu.add(dessert_menu)

menu = Menu('Restaurants')
menu.add(pancake_menu)
menu.add(diner_menu)

