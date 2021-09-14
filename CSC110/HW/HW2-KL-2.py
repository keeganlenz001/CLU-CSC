# Name: Keegan Lenz
# Date: 9/13/2021
# Project Description: Takes 4 floating point numbers from user and prints the sum


result = 0


def get_input():
    try:
        global result
        result = result + float(input())
    except ValueError:
        print('Please enter a valid input!')
        get_input()


def add_4_floats():
    for i in range(4):
        print('Please input floating point number', i + 1)
        get_input()
    print(result)


add_4_floats()