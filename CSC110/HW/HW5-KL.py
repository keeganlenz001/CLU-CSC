# Name: Keegan Lenz
# Date: 9/30/2021
# Project Description: Helps user practice arithmetic
import random
difficulty = ''
operator = ''

num1 = 0
num2 = 0
user_answer = 0
answer = 0


def get_difficulty():
    global difficulty

    difficulty = input('Would you like a Easy, Medium, or Hard problem? ')
    if difficulty != 'Easy' and difficulty != 'Medium' and difficulty != 'Hard':
        print('Make sure you spelled your difficulty correctly (Case Sensitive)')
        get_difficulty()
    get_operator()


def get_operator():
    global operator

    operator = input('What operator would you to practice with (+, -, *, /, %) ')
    if operator != '+' and operator != '-' and operator != '*' and operator != '/' and operator != '%':
        print('Please enter a valid operator!')
        get_operator()
    calc()


def calc():
    global num1
    global num2
    global answer

    if difficulty == 'Easy':
        num1 = random.randrange(0, 10)
        num2 = random.randrange(0, 10)
    elif difficulty == 'Medium':
        num1 = round(random.uniform(0, 100), 2)
        num2 = round(random.uniform(0, 100), 2)
    elif difficulty == 'Hard':
        num1 = round(random.uniform(0, 1000), 2)
        num2 = round(random.uniform(0, 1000), 2)

    if operator == '+':
        answer = num1 + num2
    elif operator == '-':
        answer = num1 - num2
    elif operator == '*':
        answer = num1 * num2
    elif operator == '/':
        answer = num1 / num2
    elif operator == '%':
        answer = num1 % num2

    get_input()


def get_input():
    global user_answer
    print('What is', num1, operator, num2)
    try:
        user_answer = float(input())
        result()
    except ValueError:
        result()


def result():
    if user_answer == answer:
        print('Good job, you got it right!')
    else:
        print('Sorry, that is the wrong answer')


get_difficulty()
