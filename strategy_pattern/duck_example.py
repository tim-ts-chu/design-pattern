#!/usr/bin/python3

import abc
import duck_module
import behavior_module

def main():
    print("Hello, duck world!")

    print("======")
    duck = duck_module.MallardDuck()
    duck.fly_behavior = behavior_module.FlyWithWings()
    duck.quack_behavior = behavior_module.Quack()
    duck.display()
    duck.swim()
    duck.performFly()
    duck.performQuack()

    print("======")
    duck = duck_module.RubberDuck()
    duck.fly_behavior = behavior_module.FlyNoWay()
    duck.quack_behavior = behavior_module.Squeak()
    duck.display()
    duck.swim()
    duck.performFly()
    duck.performQuack()

    print("======")
    duck = duck_module.RedheadDuck()
    duck.fly_behavior = behavior_module.FlyWithWings()
    duck.quack_behavior = behavior_module.Quack()
    duck.display()
    duck.swim()
    duck.performFly()
    duck.performQuack()

    print("======")
    duck = duck_module.DecoyDuck()
    duck.fly_behavior = behavior_module.FlyNoWay()
    duck.quack_behavior = behavior_module.MuteQuack()
    duck.display()
    duck.swim()
    duck.performFly()
    duck.performQuack()

if __name__ == "__main__":
    main()



