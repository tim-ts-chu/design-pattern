
import abc

class Command(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def execute(self):
        pass

class FanOnCommand(Command):
    def execute(self):
        print('Fan is turned on...')
class FanOffCommand(Command):
    def execute(self):
        print('Fan is turned off...')
class LightOnCommand(Command):
    def execute(self):
        print('Light is turned on...')
class LightOffCommand(Command):
    def execute(self):
        print('Light is turned off...')

class RemoteController:
    def __init__(self):
        self._command_slot = {}

    def set_command(self, name, command):
        self._command_slot[name] = command

    def exe_command(self, name):
        if name not in self._command_slot.keys():
            print('The action {} is not exist'.format(name))
        else:
            self._command_slot[name].execute()

class User:
    def __init__(self, controller):
        self._remote_controller = controller

    def action(self, name):
        self._remote_controller.exe_command(name)









