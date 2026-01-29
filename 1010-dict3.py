# Filename: 1010-dict3.py
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
    item = car.items()
    print(item)
    item = list(car.items())
    print(item)
    value = car.pop('color')
    print(value)
    print(car)
    value = car.pop('joe','Not found')
    print(value)
    value = car.popitem()
    print(value)
    print(car)




if __name__ == "__main__":
    main()










