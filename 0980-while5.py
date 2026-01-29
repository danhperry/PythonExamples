# Filename: 0980-while5.py
# Name: Dan Perry
# Email: dhperry@northeaststate.edu
#       danhperry@gmail.com
#       danontech@gmail.com
# Assignment:
# Date Created: Today
# Description: Write a program to find total number of
#              vowels and consonants in a string using a while loop and if else.


def main():
    str_1 = 'This is a string with a lot of information and some other information'
    cnt = 0
    v_total = 0
    c_total = 0
    while cnt < len(str_1):
        if str_1[cnt].lower() in 'aeiouy':
            v_total += 1
        else:
            c_total += 1
        cnt += 1
    print(f'Total number of vowels {v_total}')
    print(f'Total number of consonants {c_total}')








if __name__ == "__main__":
    main()










