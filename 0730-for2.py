# Filename: 0730-for2.py
# Name: Dan Perry
# Email: dhperry@northeaststate.edu
#       danhperry@gmail.com
#       danontech@gmail.com
# Assignment: for loops
# Date Created: Today
# Description: intro to for loops
#


def main():

    print('   i     i square   i cube')
    for i in range(10):
        i_sq = i**2
        i_cube = i**3
        print(f'{i:6d}{i_sq:8d}{i_cube:10d}')



    for i in range(10):
        print('   i     i square   i cube')  # headings should be before loop
        i_sq = i**2
        i_cube = i**3
        print(f'{i:6d}{i_sq:8d}{i_cube:10d}')




if __name__ == "__main__":
    main()










