# Filename: 0900-random1.py
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

    head_total = 0
    tail_total =0
    for i in range(10000):
        toss = randint(0, 1)
        if toss == 1:
            head_total += 1
        else:
            tail_total += 1
    print(f'head total = {head_total}')
    print(f'tail total = {tail_total}')
















if __name__ == "__main__":
    main()










