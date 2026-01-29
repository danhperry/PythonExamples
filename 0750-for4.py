# Filename: 0750-for4.py
# Name: Dan Perry
# Email: dhperry@northeaststate.edu
#       danhperry@gmail.com
#       danontech@gmail.com
# Assignment: for loops
# Date Created: Today
# Description: intro to for loops
#


def main():
    print('   i      i square    i cube')
    for i in range(0, 21):
        i = float(i/2)
        i_sq = i ** 2
        i_cube = i ** 3
        print(f'{i:6.2f}{i_sq:8.2f}{i_cube:11.2f}')




if __name__ == "__main__":
    main()










