# Filename: 0830-round.py
# Name: Dan Perry
# Email: dhperry@northeaststate.edu
#       danhperry@gmail.com
#       danontech@gmail.com
# Assignment: for loops
# Date Created: Today
# Description: intro to for loops
#


def main():
    numbers = [2.6157, 3.5, 5.225, 1592.995, 6.951]
    print(f'{numbers[0]}  {round(numbers[0],2)}')
    print(f'{numbers[2]}  {round(numbers[2],1)}')
    print(f'{numbers[3]}  {round(numbers[3],0)}')
    print(f'{numbers[3]}  {round(numbers[3], -1)}')
    total = 0
    r_total = 0
    print('not rounded  rounded')
    for number in numbers:
        r_number = round(number,2)
        total += number
        r_total += r_number
        print(f'{number:8.2f}  {r_number:8.2f}')
    print(f'{total:8.2f}  {r_total:8.2f}')








if __name__ == "__main__":
    main()










