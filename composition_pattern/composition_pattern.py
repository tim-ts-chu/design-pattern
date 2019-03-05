#!/usr/bin/python3

import menu_module

class Waitress:
    def show_menu(self, menu):
        menu.traverse('show')

def main():
    w = Waitress()
    w.show_menu(menu_module.menu)

if __name__ == '__main__':
    main()
