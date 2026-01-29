# Filename: 0870-math3.py
# Name: Dan Perry
# Email: dhperry@northeaststate.edu
#       danhperry@gmail.com
#       danontech@gmail.com
# Assignment: for loops
# Date Created: Today
# Description: math trig functions
#

import time
import math as m



def main():
    degree = 90
    print(degree)
    radian = m.radians(degree)
    print(radian)
    sin = m.sin(radian)
    print(sin)
    print('  degree  radians   sine  cosine  tangent')
    for angle_d in range(0,91,5):
        angle_r = m.radians(angle_d)
        sine = m.sin(angle_r)
        cosine = m.cos(angle_r)
        tangent = m.tan(angle_r)
        print(f'{angle_d:8.3f}{angle_r:8.3f}{sine:8.3f}{cosine:8.3f}{tangent:8.3f}')










if __name__ == "__main__":
    main()










