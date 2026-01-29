# Filename: 0550-or4.py
# Name: Dan Perry
# Email: dhperry@northeaststate.edu
#       danhperry@gmail.com
#       danontech@gmail.com
# Assignment: Logic
# Date Created: Today
# Description: OR
#


def main():
    temp_f = float(input("Enter temperature in Fahrenheit: "))
    press_psi = float(input("Enter pressure in psi: "))
    if temp_f > 40 or press_psi > 50:
        print(f'The temperature or pressure is high')
    elif temp_f > 40 or press_psi < 50:
        print(f'The temperature is high or pressure is low')
    elif temp_f < 40 or press_psi > 50:  # never be true
        print(f'The temperature is low or pressure is high')
    else:
        print(f'Things are normal')




if __name__ == "__main__":
    main()
