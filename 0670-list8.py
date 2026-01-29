# Filename: 0670-list8.py
# Name: Dan Perry
# Email: dhperry@northeaststate.edu
#       danhperry@gmail.com
#       danontech@gmail.com
# Assignment: Lists
# Date Created: Today
# Description:
#


def main():

    names = ['Graham', 'John', 'Terry', 'Eric', 'Terry', 'Michael']
    l = names.copy()
    print(id(l))
    print(id(names))
    l1 = names
    print(id(l1))
    print(id(names))
    l.pop()
    print(l)
    print(names)
    l1.pop(0)
    print(l1)
    print(names)



if __name__ == "__main__":
    main()
