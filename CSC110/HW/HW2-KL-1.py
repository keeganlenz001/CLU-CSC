# Name: Keegan Lenz
# Date: 9/13/2021
# Project Description: Takes 4 integer numbers from user keyboard and prints the addition results to the display


result = 0


def get_input():
    try:
        global result
        result = result + int(input())
    except ValueError:
        print('Please enter a valid input!')
        get_input()


def add_4_ints():
    for i in range(4):
        print('Please input integer number', i + 1)
        get_input()
    print(result)


add_4_ints()
