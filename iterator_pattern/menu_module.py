
import abc

class Menu(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def create_iterator(self):
        pass

class Iterator(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get(self):
        pass
    @abc.abstractmethod
    def has_next(self):
        pass
    @abc.abstractmethod
    def next(self):
        pass

class PancakeMenu(Menu):

    def __init__(self):
        self.menu_items = []
        self.item_dollars = []

        self.menu_items.append('Regular Pancake')
        self.item_dollars.append(2.99)

        self.menu_items.append('Cheese Pancake')
        self.item_dollars.append('3.50')

        self.menu_items.append('Bacon Pancake')
        self.item_dollars.append('3.99')

    def create_iterator(self):
        return PancakeMenuIterator(self.menu_items, self.item_dollars)

class DinerMenu(Menu):
    def __init__(self):
        self.menu_items = {}
        self.menu_items['Pasta'] = 3.99
        self.menu_items['Pizza'] = 4.99
        self.menu_items['Hamburger'] = 3.49

    def create_iterator(self):
        return DinerMenuIterator(self.menu_items)

class PancakeMenuIterator(Iterator):
    def __init__(self, menu_items, item_dollars):
        self.menu_items = menu_items
        self.item_dollars = item_dollars
        self._curr = 0
        self._item_len = len(menu_items)
    def get(self):
        return (self.menu_items[self._curr], self.item_dollars[self._curr])
    def has_next(self):
        return self._curr < self._item_len - 1
    def next(self):
        if self._curr < self._item_len - 1:
            self._curr += 1
        else:
            raise IndexError

class DinerMenuIterator(Iterator):
    def __init__(self, menu_items):
        self.menu_items = menu_items
        self.item_names = list(menu_items.keys())
        self._curr = 0
        self._item_len = len(self.item_names)
    def get(self):
        name = self.item_names[self._curr]
        return (name, self.menu_items[name])
    def has_next(self):
        return self._curr < self._item_len - 1
    def next(self):
        if self._curr < self._item_len - 1:
            self._curr += 1
        else:
            raise IndexError

