# Filename: 0280-mile-meter.py
# Name: Dan Perry
#Email: dhperry@northeaststate.edu
#       danhperry@gmail.com
#       danontech@gmail.com
# Assignment: String manipulation
# Date Created: Today
# Description: This program will ask the user to enter a number of feet
#              and convert that information to inches, miles, and meters.


def main():
    feet = float(input('Enter the number of feet: '))
    mile = feet/5280
    inches = feet * 12
    cm = inches /2.54
    meter = cm / 100
    print('Feet:', feet)
    print('Mile:', mile)
    print('Inches:', inches)
    print('CM:', cm)
    print('Meter:', meter)





if __name__ == "__main__":
    main()
