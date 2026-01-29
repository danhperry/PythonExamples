# Filename: 0450-ifelif2.py
# Name: Dan Perry
# Email: dhperry@northeaststate.edu
#       danhperry@gmail.com
#       danontech@gmail.com
# Assignment: Logic
# Date Created: Today
# Description: Take a numeric grade and find a letter grade
#


def main():

    grade = int(input('Enter your grade: '))
    if grade >= 90:
        print('Your grade is A')
    elif grade >= 80:
        print('Your grade is B')
    elif grade >= 70:
        print('Your grade is C')
    elif grade >= 65:
        print('Your grade is D')
    else:
        print('Your grade is F')





if __name__ == "__main__":
    main()
