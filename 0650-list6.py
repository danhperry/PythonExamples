# Filename: 0630-list4.py
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
    pos = names.index('Graham')
    print(pos)
    pos = names.index('Terry')
    print(pos)
    pos = names.index('Terry', 3)
    print(pos)
    pos = names.index('Terry',1, 3)
    print(pos)

    cnt = names.count('Terry')
    print(cnt)
    cnt = names.count('Joan')
    if cnt > 0:
        idx = names.index('Joan')
        print(names[idx])
    else:
        print('no name')
    cnt = names.count('John')
    if cnt > 0:
        idx = names.index('John')
        print(names[idx])
    else:
        print('no name')








if __name__ == "__main__":
    main()
