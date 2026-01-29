# Filename: 0760-for5.py
# Name: Dan Perry
# Email: dhperry@northeaststate.edu
#       danhperry@gmail.com
#       danontech@gmail.com
# Assignment: for loops
# Date Created: Today
# Description: intro to for loops
#


def main():
    numbers = [1, 5, 11.5, 14, 4, 1.2]
    for i in numbers:
        print(i)
    print('  i     j')
    for i in numbers:
        i = float(i)
        j = i * 3

        print(f'{i:6.2f}{j:8.2f}')






if __name__ == "__main__":
    main()










