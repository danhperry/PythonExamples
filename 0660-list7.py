# Filename: 06360-list7.py
# Name: Dan Perry
# Email: dhperry@northeaststate.edu
#       danhperry@gmail.com
#       danontech@gmail.com
# Assignment: Lists
# Date Created: Today
# Description: removing items from a list
#


def main():

    names = ['Graham', 'John', 'Terry', 'Eric', 'Terry', 'Michael']
    print(names)
    names.pop()
    print(names)
    names.pop(1)
    print(names)
    name = names.pop()
    print(name)
    print(names)
    names = ['Graham', 'John', 'Terry', 'Eric', 'Terry', 'Michael']
    print(names)
    names.remove('Terry')
    print(names)
    if names.count('Joan') > 0:
        names.remove('Joan')
        print(f'Joan removed')
    else:
        print('no joan')
    print(names)
    name = 'Graham'
    if names.count(name) > 0:
        names.remove(name)
        print(f'{name} removed')
    else:
        print(f'no {name}')
    print(names)

if __name__ == "__main__":
    main()
