#!/usr/bin/python3

import factory_module

def main():
    print('Hello pizza world')
    ny_store = factory_module.NYPizzaStore()

    pizza = ny_store.orderPizza('Cheese')
    print('Get pizza:', pizza.show())
    pizza = ny_store.orderPizza('Veggie')
    print('Get pizza:', pizza.show())

    chicago_store = factory_module.ChicagoPizzaStore()

    pizza = chicago_store.orderPizza('Clam')
    print('Get pizza:', pizza.show())

if __name__ == '__main__':
    main()
