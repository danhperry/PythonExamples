# Filename: 0630-list4.py
# Name: Dan Perry
# Email: dhperry@northeaststate.edu
#       danhperry@gmail.com
#       danontech@gmail.com
# Assignment: Lists
# Date Created: Today
# Description: slicing list elements
#


def main():

    names = ['Graham', 'John', 'Terry', 'Eric', 'Terry', 'Michael']
    print(names)
    names.append('James')
    print(names)
    names.append('John')
    print(names)
    names.insert(2, 'Betty')
    print(names)
    names.extend(['Bill', 'John'])
    print(names)
    n1 = ['Mary', 'Jane', 'Cindy']
    names.extend(n1)
    print(names)









if __name__ == "__main__":
    main()
