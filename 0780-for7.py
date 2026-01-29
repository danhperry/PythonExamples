# Filename: 0780-for7.py
# Name: Dan Perry
# Email: dhperry@northeaststate.edu
#       danhperry@gmail.com
#       danontech@gmail.com
# Assignment: for loops
# Date Created: Today
# Description: intro to for loops
#


def main():
    '''
    names = []
    for i in range(5):
        name = input('Enter a name: ')
        names.append(name)
    print(names)

    names = []
    for i in range(5):
        name = input('Enter a name: (Enter to exit)')
        if name != '':
            names.append(name)
        else:
            break
    print(names)
    '''
    names = []
    for i in range(5):
        name = input('Enter a name: (Enter to exit)')
        if name != '':
            names.append(name)
        else:
            continue
    print(names)










if __name__ == "__main__":
    main()










