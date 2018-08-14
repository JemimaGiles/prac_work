usernames = ['jimbo', 'glitson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

ask_username = input("what is your username? ")

if ask_username in usernames:
    print("welcome")
else:
    print("Access Denied")
