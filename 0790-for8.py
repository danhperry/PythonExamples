# Filename: 0790-for8.py
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


    grade = 0
    total = 0
    for i in range(5):
        grade = int(input('Enter a grade: '))
        total = total + grade
    print(f'The total is {total}')
    '''

    total = 0
    cnt = 0
    for i in range(15):
        grade = int(input('Enter a grade: (-1 to exit) '))
        if grade == -1:
            break

        total += grade
        cnt += 1
    avg = total / cnt
    print(f'The average is {avg:8.2f}')
    print(f'The total is {total}')











if __name__ == "__main__":
    main()










