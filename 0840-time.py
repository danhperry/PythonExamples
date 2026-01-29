# Filename: 0840-time.py
# Name: Dan Perry
# Email: dhperry@northeaststate.edu
#       danhperry@gmail.com
#       danontech@gmail.com
# Assignment: for loops
# Date Created: Today
# Description: time library and sleep
#
import time

def main():
    print(f'Hello, world!')
    time.sleep(.5)
    print(f'goodbye, world!')
    print('Countdown')
    for x in range(10,-1, -1):
        print(x)
        time.sleep(1)
    print('Blastoff')






if __name__ == "__main__":
    main()










