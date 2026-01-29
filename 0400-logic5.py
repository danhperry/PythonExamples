# Filename: 0400-logic5.py
# Name: Dan Perry
# Email: dhperry@northeaststate.edu
#       danhperry@gmail.com
#       danontech@gmail.com
# Assignment: Logic
# Date Created: Today
# Description: This program will show an example of using if statements.
#


def main():

    oz = float(input('Enter the number of ounces: '))
    if oz >= 16:
        pint = oz/8
        print(f'{oz:.2f} ounces = {pint:.2f} pints')
    if oz < 16:
        ml = oz * 29.57
        print(f'{oz:.2f} ounces = {ml:.2f} ml')











if __name__ == "__main__":
    main()
