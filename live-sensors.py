import os
import time
from colorama import Fore, Style, init
from getBanner import printBanner
from options import printOptions

init(autoreset=True)

while True:
    printBanner()
    printOptions()

    action = input(Fore.GREEN+'Select an action: \n')

    if action == '0':
        print('Setup starting...')
        time.sleep(1)
        print('Updating system...')
        os.system('sudo apt update -y')
        print('Installing packages...')
        os.system('sudo apt install lm-sensors -y')
        print('Packages installed!')
        time.sleep(1)
        input('Press any key to continue...')
    elif action == '2':
        refreshRate = int(input('Please set interval in seconds...\n'))
    elif action == '1':
        while True:
            os.system('clear')
            os.system('sensors')
            try:
                time.sleep(refreshRate)
            except NameError:
                time.sleep(1)
    elif action == '99':
        print('Goodbye, Thanks for using LiveSensors.')
        break


