# Filename: 1020-dict4.py
# Name: Dan Perry
# Email: dhperry@northeaststate.edu
#       danhperry@gmail.com
#       danontech@gmail.com
# Assignment:
# Date Created: Today
# Description: Start looking at dictionaries


def main():
    car = {'make': 'Ford',
           'model': 'Mustang',
           'year': 1964,
           'color': 'blue'
           }
    new_car = {'engine': '454',
               'transmission': 'manual'}
    car.update(new_car)
    print(car)
    car = {'make': 'Ford',
           'model': 'Mustang',
           'year': 1964,
           'color': 'blue'
           }
    new_car = {'engine': '454',
               'transmission': 'manual',
               'color': 'red'}
    car.update(new_car)
    print(car)
    new_car = [('engine', '789'),('transmission', 'xxxx')]
    car.update(new_car)
    print(car)



if __name__ == "__main__":
    main()










