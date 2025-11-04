# Filename: 0240-stringmanip.py
# Name: Dan Perry
# Email: dhperry@northeaststate.edu
#        danhperry@gmail.com
#        danontech@gmail.com
# Assignment: String manipulation
# Date Created: Today
# Description: This is an example of using string
#              manipulation. The program will ask
#              the user for some information and
#              make changes to the information.


def main():
    f_name = input('Enter full name: ')
    address = input('Enter address: ')
    print('Full name:', f_name)
    print('Address:', address)
    f_name1 = f_name.upper()
    print('Full name:', f_name1)
    address = address.title()
    print('Address', address)
    lis = f_name1.split()
    print(lis)
    print('Last name:', lis[-1])
    print('First name:', lis[0])

if __name__ == "__main__":
    main()
