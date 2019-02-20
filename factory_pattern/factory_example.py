#!/usr/bin/Python3

import factory_module

ny_store = factory_module.NYPizzaStore()

pizza = ny_store.order('Chieese')
pizza = ny_store.order('Veggie')

chicago_store = factory_module.ChicagoPizzaStore()

pizza = chicago_store.order('Clam')

def main():
    print('Hello pizza world')

if __name__ == '__main__':
    main()
