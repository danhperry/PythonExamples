# Filename: 0580-andorpy
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
    y = 1
    z = 10
    if x == 10 and y == 10 or z == 10:
        print('True')
    else:
        print('False')

    if x == 10 and (y == 10 or z == 10):
        print('True')
    else:
        print('False')


if __name__ == "__main__":
    main()
