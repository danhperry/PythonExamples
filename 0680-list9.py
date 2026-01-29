# Filename: 0680-list9.py
# Name: Dan Perry
# Email: dhperry@northeaststate.edu
#       danhperry@gmail.com
#       danontech@gmail.com
# Assignment: Lists
# Date Created: Today
# Description: sorting lists
#


def main():

    names = ['Graham', 'John', 'Terry', 'Eric', 'Terry', 'Michael']
    names.reverse()
    print(names)
    names.sort()
    print(names)
    names.sort(reverse=True)
    print(names)
    names = ['Graham', 'John', 'Terry', 'Eric', 'Terry', 'Michael']
    names1 = sorted(names)
    print(names1)
    print(names)
    names1 = sorted(names, reverse=True)
    print(names1)
    numbers = [1, 0, 2, 42, -4]
    numbers.sort()
    print(numbers)
    numbers.clear()
    print(numbers)


if __name__ == "__main__":
    main()
