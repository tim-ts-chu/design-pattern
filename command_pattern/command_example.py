#!/usr/bin/python3

import command_module

def main():
    remote_controller = command_module.RemoteController()

    remote_controller.set_command('lightOn', command_module.LightOnCommand())
    remote_controller.set_command('lightOff', command_module.LightOffCommand())
    remote_controller.set_command('fanOn', command_module.FanOnCommand())
    remote_controller.set_command('fanOff', command_module.FanOffCommand())

    user = command_module.User(remote_controller)

    user.action('fanOn')
    user.action('lightOn')
    user.action('lightOff')
    user.action('fanOff')

if __name__ == '__main__':
    main()
