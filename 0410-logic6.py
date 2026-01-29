# Filename: 0410-logic6.py
# Name: Dan Perry
# Email: dhperry@northeaststate.edu
#       danhperry@gmail.com
#       danontech@gmail.com
# Assignment: Logic
# Date Created: Today
# Description: This program will show an example of using nested if statements.
#


def main():

    grade = int(input('Enter your grade: '))
    if grade == 1:
        color = input('Enter your color: ')
        if color.lower() == 'red':
            print('Your favorite color is red')
        if color.lower() == 'green':
            print('Your favorite color is green')
    if grade >= 2:
        movie = input('Enter your favorite movie: ')
        if movie.lower() == 'xyz':
            print('Your favorite movie is xyz ')









if __name__ == "__main__":
    main()
