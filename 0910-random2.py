# Filename: 0910-random1.py
# Name: Dan Perry
# Email: dhperry@northeaststate.edu
#       danhperry@gmail.com
#       danontech@gmail.com
# Assignment:
# Date Created: Today
# Description: random functions
#

from random import randrange, randint


def main():
    roll = [0, 0, 0, 0, 0, 0, 0]
    for i in range(10000000):
        r = randrange(1, 7)
        roll[r] += 1
    print(f'Roll of 1 = {roll[1]}')
    print(f'Roll of 2 = {roll[2]}')
    print(f'Roll of 3 = {roll[3]}')
    print(f'Roll of 4 = {roll[4]}')
    print(f'Roll of 5 = {roll[5]}')
    print(f'Roll of 6 = {roll[6]}')




















if __name__ == "__main__":
    main()










