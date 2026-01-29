# Filename: 0430-ifelse2.py
# Name: Dan Perry
# Email: dhperry@northeaststate.edu
#       danhperry@gmail.com
#       danontech@gmail.com
# Assignment: Logic
# Date Created: Today
# Description: Take a numeric grade and find a letter grade
#


def main():

    grade = int(input('Enter a grade: '))
    if grade >= 65:
        if grade >= 70:
            if grade >= 80:
                if grade >= 90:
                    print('Your grade is an A')
                else:
                    print('Your grade is a B')

            else:
                print('Your grade is a C')

        else:
            print('Your grade is a D')

    else:
        print('Your grade is an F')









if __name__ == "__main__":
    main()
