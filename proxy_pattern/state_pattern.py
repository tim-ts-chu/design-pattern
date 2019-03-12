#!/usr/bin/python3

import state_module

def main():
    gm = state_module.GumballMachine(5)
    print('should be in no quarter state...')
    print('try turn crank...')
    gm.turn_crank()
    print('try eject quarter...')
    gm.eject_quarter()
    print('try dispense...')
    gm.dispense()
    print('try insert quarter...')
    gm.insert_quarter()

    print('should be in has quarter state...')
    print('try insert quarter...')
    gm.insert_quarter()
    print('try dispense...')
    gm.dispense()
    print('try eject quarter...')
    gm.eject_quarter()

    print('should be in no quarter state...')
    print('try insert quarter...')
    gm.insert_quarter()

    print('should be in has quarter state...')
    print('try turn crank...')
    gm.turn_crank()

    print('try insert quarter...')
    gm.insert_quarter()
    print('try turn crank...')
    gm.turn_crank()

    print('try insert quarter...')
    gm.insert_quarter()
    print('try turn crank...')
    gm.turn_crank()

    print('try insert quarter...')
    gm.insert_quarter()
    print('try turn crank...')
    gm.turn_crank()

    print('should be in sold out state...')
    print('try insert quarter...')
    gm.insert_quarter()
    print('try eject quarter...')
    gm.eject_quarter()
    print('try turn crank...')
    gm.turn_crank()
    print('try dispense...')
    gm.dispense()


if __name__ == '__main__':
    main()
