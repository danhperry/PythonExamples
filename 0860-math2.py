# Filename: 0860-math2.py
# Name: Dan Perry
# Email: dhperry@northeaststate.edu
#       danhperry@gmail.com
#       danontech@gmail.com
# Assignment: for loops
# Date Created: Today
# Description: math floor ceiling absolute value
#

import time
import math as m



def main():
    n1 = 3.5
    n2 = -3.5
    n3 = 5.9
    print(f'Absolute value {abs(n1)} {abs(n2)} {abs(n3)}')
    print(f'floating absolute value {m.fabs(n1)} {m.fabs(n2)} {m.fabs(n3)}')
    print(f'Ceiling {m.ceil(n1)} {m.ceil(n2)} {m.ceil(n3)}')
    print(f'Floor {m.floor(n1)} {m.floor(n2)} {m.floor(n3)}')







if __name__ == "__main__":
    main()










