# Filename: 0510-and5.py
# Name: Dan Perry
# Email: dhperry@northeaststate.edu
#       danhperry@gmail.com
#       danontech@gmail.com
# Assignment: Logic
# Date Created: Today
# Description: And
#


def main():

    temp_f = float(input("Enter temperature in Fahrenheit: "))
    press_psi = float(input("Enter pressure in psi: "))
    if temp_f>40 and press_psi>50:
        print(f'The temperature and pressure are high')
    elif temp_f<=40 and press_psi>50:
        print(f'The pressure is high')
    elif temp_f > 40 and press_psi<=50:
        print(f'The temperature is high')
    else:
        print(f'The temperature and pressure are low')





if __name__ == "__main__":
    main()
