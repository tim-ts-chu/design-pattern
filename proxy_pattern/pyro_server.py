#!/usr/bin/python3

import Pyro4
import state_module

def main():
    '''
    daemon = Pyro4.Daemon('localhost')
    ns = Pyro4.locateNS()
    uri = daemon.register(state_module.GumballMachine)
    ns.register("GumballMachine", uri)
    daemon.requestLoop()
    '''
    Pyro4.Daemon.serveSimple(
    {
        state_module.GumballMachine: "example.GumballMachine"
    },
    host='localhost', port=9090, ns = False, verbose=True)
if __name__ == '__main__':
    main()
