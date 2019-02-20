#!/usr/bin/python3

import decorator_module

class MochaHouseBlend(decorator_module.HouseBlend):
    @decorator_module.Mocha('description')
    def getDescription(self):
        return super().getDescription()

    @decorator_module.Mocha('cost')
    def cost(self):
        return super().cost()

class MilkEspresso(decorator_module.Espresso):
    @decorator_module.Milk('description')
    def getDescription(self):
        return super().getDescription()

    @decorator_module.Milk('cost')
    def cost(self):
        return super().cost()

class WhipSoyDecaf(decorator_module.Decaf):
    @decorator_module.Whip('description')
    @decorator_module.Soy('description')
    def getDescription(self):
        return super().getDescription()

    @decorator_module.Whip('cost')
    @decorator_module.Soy('cost')
    def cost(self):
        return super().cost()

class WhipSoyMochaDarkRoast(decorator_module.DarkRoast):
    @decorator_module.Whip('description')
    @decorator_module.Soy('description')
    @decorator_module.Mocha('description')
    def getDescription(self):
        return super().getDescription()

    @decorator_module.Whip('cost')
    @decorator_module.Soy('cost')
    @decorator_module.Mocha('cost')
    def cost(self):
        return super().cost()

def main():
    print("Hello, decorator world!")

    print("===============")
    b = decorator_module.HouseBlend()
    print(b.getDescription())
    print(b.cost())

    print("===============")
    b = MochaHouseBlend()
    print(b.getDescription())
    print(b.cost())

    print("===============")
    b = MilkEspresso()
    print(b.getDescription())
    print(b.cost())

    print("===============")
    b = WhipSoyDecaf()
    print(b.getDescription())
    print(b.cost())

    print("===============")
    b = WhipSoyMochaDarkRoast()
    print(b.getDescription())
    print(b.cost())

if __name__ == "__main__":
    main()
