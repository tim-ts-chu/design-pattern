#!/usr/bin/python3
import sys
import Pyro4
import state_module


def main():
    sys.excepthook = Pyro4.util.excepthook
    gumballMachine = Pyro4.Proxy('PYRO:example.GumballMachine@localhost:9090')
    gumballMachine.set_candy_amount(3)

    print(gumballMachine.insert_quarter())
    print(gumballMachine.eject_quarter())
    print(gumballMachine.turn_crank())
    print(gumballMachine.insert_quarter())
    print(gumballMachine.turn_crank())

if __name__ == '__main__':
    main()


