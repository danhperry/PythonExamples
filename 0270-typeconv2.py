# Filename: 0270-typeconv2.py
# Name: Dan Perry
#Email: dhperry@northeaststate.edu
#       danhperry@gmail.com
#       danontech@gmail.com
# Assignment: String manipulation
# Date Created: Today
# Description: This example will show how to convert input strings to numbers


def main():
    st = input('Enter a string: ')
    print(type(st))
    num = input('Enter a integer: ')
    print(type(num))
    num = int(num)
    print(type(num))
    num = input('Enter a floating point number: ')
    print(type(num))
    num = float(num)
    print(type(num))
    num = int(input('Enter a integer: '))
    print(type(num))




if __name__ == "__main__":
    main()
