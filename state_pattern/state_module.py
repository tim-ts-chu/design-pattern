
import abc

class State(metaclass=abc.ABCMeta):

    def __init__(self, gumball_machine):
        self._gm = gumball_machine

    # force all states to impelment these actions
    @abc.abstractmethod
    def insert_quarter(self):
        pass
    @abc.abstractmethod
    def eject_quarter(self):
        pass
    @abc.abstractmethod
    def turn_crank(self):
        pass
    @abc.abstractmethod
    def dispense(self):
        pass

class NoQuarterState(State):
    def insert_quarter(self):
        print('A quarter was put in.')
        self._gm.change_state(HasQuarterState(self._gm))
    def eject_quarter(self):
        print('No quarter can be eject.')
    def turn_crank(self):
        print('Please insert a quarter first.')
    def dispense(self):
        print('Please insert a quarter first.')

class HasQuarterState(State):
    def insert_quarter(self):
        print('You already have inserted a quarter.')
    def eject_quarter(self):
        print('Reture a quarter back.')
        self._gm.change_state(NoQuarterState(self._gm))
    def turn_crank(self):
        print('Crank turned and wait for the result.')
        if self._gm.get_candy_amount() == 1:
            print('You gonna get a candy.')
            self._gm.change_state(SoldState(self._gm)) # SoldState is a transition state
            self._gm.dispense() # make action continuousely be executed
        else:
            import random
            if random.randint(0, 10)%2 == 0:
                print('Congratulation!! You have won double candies this time.')
                self._gm.change_state(WinnerState(self._gm)) # WinnerState is a transition state
                self._gm.dispense() # make action continuousely be executed
            else:
                print('You gonna get a candy.')
                self._gm.change_state(SoldState(self._gm)) # SoldState is a transition state
                self._gm.dispense() # make action continuousely be executed
    def dispense(self):
        print('Please turn the crank before hand.')

class SoldState(State):
    def insert_quarter(self):
        print('Please wait for dispensing candy(ies).')
    def eject_quarter(self):
        print('Please wait for dispensing candy(ies).')
    def turn_crank(self):
        print('Please wait for dispensing candy(ies).')
    def dispense(self):
        self._gm.release_candy(1)
        if self._gm.get_candy_amount() > 0:
            self._gm.change_state(NoQuarterState(self._gm))
        else:
            self._gm.change_state(SoldOutState(self._gm))

class WinnerState(State):
    def insert_quarter(self):
        print('Please wait for dispensing candy(ies).')
    def eject_quarter(self):
        print('Please wait for dispensing candy(ies).')
    def turn_crank(self):
        print('Please wait for dispensing candy(ies).')
    def dispense(self):
        self._gm.release_candy(2)
        if self._gm.get_candy_amount() > 0:
            self._gm.change_state(NoQuarterState(self._gm))
        else:
            self._gm.change_state(SoldOutState(self._gm))

class SoldOutState(State):
    def insert_quarter(self):
        print('The gumball machine has sold out.')
    def eject_quarter(self):
        print('The gumball machine has sold out.')
    def turn_crank(self):
        print('The gumball machine has sold out.')
    def dispense(self):
        print('The gumball machine has sold out.')

class GumballMachine:
    def __init__(self, num_of_gaumball):
        self._num_of_gaumball = num_of_gaumball
        if num_of_gaumball > 0:
            self._state = NoQuarterState(self)
        else:
            self._state = SoldOutState(self)

    def get_candy_amount(self):
        return self._num_of_gaumball

    def change_state(self, state):
        print('State:{}'.format(type(state)))
        self._state = state

    def release_candy(self, num):
        print('Gumball machine release {} candy(ies)'.format(num))
        self._num_of_gaumball -= num

    # state actions exposed by gumball machine
    def insert_quarter(self):
        self._state.insert_quarter()

    def eject_quarter(self):
        self._state.eject_quarter()

    def turn_crank(self):
        self._state.turn_crank()

    def dispense(self):
        self._state.dispense()

