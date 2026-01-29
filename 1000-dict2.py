# Filename: 1000-dict2.py
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
    car2 = car
    print(id(car))
    print(id(car2))
    car2['engine'] = 454
    print(id(car))
    print(id(car2))
    print(car)
    print(car2)
    car3 = car2.copy()
    print(id(car3))
    car3['engine'] = 357
    print(car3)
    print(car)
    car3.clear()
    print(car3)
    key = car.keys()
    print(key)
    key = list(key)
    print(key)
    value = car.values()
    print(value)
    value = list(value)
    print(value)




if __name__ == "__main__":
    main()










