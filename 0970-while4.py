# Filename: 0970-while4.py
# Name: Dan Perry
# Email: dhperry@northeaststate.edu
#       danhperry@gmail.com
#       danontech@gmail.com
# Assignment:
# Date Created: Today
# Description: While loops


def main():

    total = 0
    grade = 0
    grade_list = []
    while grade != -1:
        grade = int(input('Enter a grade: (-1 to exit)'))
        if grade < -1 or grade > 100:
            print('Enter a number between -1 and 100')
            continue

        if grade != -1:
            total += grade
            grade_list.append(grade)
    print(grade_list)
    print(f' Grade total {total}')
    avg = total / len(grade_list)
    print(f'Average grade is {avg}')







if __name__ == "__main__":
    main()










