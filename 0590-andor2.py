# Filename: 0590-andor2.py
# Name: Dan Perry
# Email: dhperry@northeaststate.edu
#       danhperry@gmail.com
#       danontech@gmail.com
# Assignment: Logic
# Date Created: Today
# Description: and OR
#


def main():
    x = 10
    y = 10
    z = 1
    if (x == 10 and y == 10) or (z == 10 and x < 10):
        print('True')
    else:
        print('False')

    if (x == 10 and (y == 10 or z == 10)) and x < 10:
        print('True')
    else:
        print('False')




if __name__ == "__main__":
    main()
