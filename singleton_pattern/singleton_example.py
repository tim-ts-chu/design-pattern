#!/usr/bin/python3

import time
import threading
import singleton_module

class MySingleton(singleton_module.Singleton):
    """
    Singleton class is easy to implement. Thus, we don't suggest to inherit it.
    Instead, you can directly your singleton class by the same way to reduce
    the complexity of you code.
    """
    pass

class MyThread(threading.Thread):
    def __init__(self, idx):
        self._idx = idx
        self._singleton_instance = None
        threading.Thread.__init__(self)

    def run(self):
        t1 = time.time()
        self.get_singleton()
        t2 = time.time()
        print("time = [{0}]".format(t2 - t1))
        self.print_singleton()

    def get_singleton(self):
        self._singleton_instance = MySingleton()

    def print_singleton(self):
        print("instance = [{0}]".format(self._singleton_instance))

def main():
    print("Hello, singleton world!")

    t1 = MyThread(1)
    t2 = MyThread(2)
    t3 = MyThread(3)
    t4 = MyThread(4)

    t1.start()
    t2.start()
    t3.start()
    t4.start()

if __name__ == "__main__":
    main()

