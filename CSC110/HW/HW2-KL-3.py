# Name: Keegan Lenz
# Date: 9/13/2021
# Project Description: Takes 2 integer and 2 floating point numbers and print the sum


result = 0


def get_int():
    try:
        global result
        result = result + int(input())
    except ValueError:
        print('Please enter a valid input!')
        get_int()


def get_float():
    try:
        global result
        result = result + float(input())
    except ValueError:
        print('Please enter a valid input!')
        get_float()


def get_sum():
    for i in range(2):
        print('Please input integer number', i + 1)
        get_int()

    for i in range(2):
        print('Please input floating point number', i + 1)
        get_float()

    print(result)


get_sum()


