# Filename: 0690-list10.py
# Name: Dan Perry
# Email: dhperry@northeaststate.edu
#       danhperry@gmail.com
#       danontech@gmail.com
# Assignment: Lists
# Date Created: Today
# Description: if with lists
#


def main():

    names = ['Graham', 'John', 'Terry', 'Eric', 'Terry', 'Michael']
    name = 'Johnny'
    if name in names:
        print(name)
    else:
        print(f'{name} not in list')
    if name not in names:
        print(f'{name} not in list')

    else:
        print(f'{name}  in list')
    if name in names:
        names.remove(name)
        print(f'{name} removed from list')
    else:
        print(f'{name} not in list')
    print(names)





if __name__ == "__main__":
    main()
