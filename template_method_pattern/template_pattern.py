#!/usr/bin/python3

import sort_module

class Duck:
    def __init__(self, size):
        self._size = size

    def __str__(self):
        return ' ' + self._size + ' '

    def get_size(self):
        return self._size

def duck_compare(duck1, duck2):
    if duck1.get_size() > duck2.get_size():
        return True
    else:
        return False

def main():
    ducks = []
    for i in range(0, 10):
        import random
        d = Duck(random.randint(0, 100))
        print('Duck size:{}'.format(d.get_size()))
        ducks.append(d)


    qs = sort_module.QuickSort()
    qs.setCompareMethod(duck_compare)
    ducks = qs.sort(ducks)

    print('=== after sort ==')
    for d in ducks:
        print('Duck size:{}'.format(d.get_size()))

if __name__ == '__main__':
    main()

