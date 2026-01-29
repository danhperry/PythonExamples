# Filename: 0460-if-elif2.py
# Name: Dan Perry
# Email: dhperry@northeaststate.edu
#       danhperry@gmail.com
#       danontech@gmail.com
# Assignment: Logic
# Date Created: Today
# Description: Looking at elif's
#


def main():

    game = input('Enter your favorite game: ')
    if game.lower() == 'poker':
        print('Your favorite game is poker')
        hand = input('Do you have a good hand: ')
        print(f'It is a good {hand}')
    elif game.lower() == 'jacks':
        print('I hope you have a level place to play')
    elif game.lower() == 'chicken':
        print("Don't cross the road")






if __name__ == "__main__":
    main()
