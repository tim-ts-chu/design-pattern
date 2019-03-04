#!/usr/bin/python3

import menu_module

class Waitress:
    def __init__(self):
        self._menus = {}
        self._menus['Pancake'] = menu_module.PancakeMenu() 
        self._menus['Diner'] = menu_module.DinerMenu() 

    def print_menu(self):

        for key in self._menus.keys():
            print('=== {} Menu ==='.format(key))
            it = self._menus[key].create_iterator()

            while(True):
                name, price = it.get()
                print('{} {}'.format(name, price))
                if (it.has_next()):
                    it.next()
                else:
                    break
def main():
    w = Waitress()
    w.print_menu()

if __name__ == '__main__':
    main()
