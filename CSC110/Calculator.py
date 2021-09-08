# Name: Keegan L.
# Date: 9/1/2021
# Project Description: Basic Calculator With User Input (Limited to Addition, Subtraction, Multiplication, Division)

# Define global variables

class Colors:
    reset = '\033[0m'
    bold = '\033[01m'
    disable = '\033[02m'
    underline = '\033[04m'
    reverse = '\033[07m'
    strikethrough = '\033[09m'
    invisible = '\033[08m'

    class Fg:
        black = '\033[30m'
        red = '\033[31m'
        green = '\033[32m'
        orange = '\033[33m'
        blue = '\033[34m'
        purple = '\033[35m'
        cyan = '\033[36m'
        lightGrey = '\033[37m'
        darkGrey = '\033[90m'
        lightRed = '\033[91m'
        lightGreen = '\033[92m'
        yellow = '\033[93m'
        lightBlue = '\033[94m'
        pink = '\033[95m'
        lightCyan = '\033[96m'

    class Bg:
        black = '\033[40m'
        red = '\033[41m'
        green = '\033[42m'
        orange = '\033[43m'
        blue = '\033[44m'
        purple = '\033[45m'
        cyan = '\033[46m'
        lightGrey = '\033[47m'


num1 = 0
num2 = 0
opp = 0
result = 0


# Gets first number; ensures input is a number
def first_number():
    global num1
    num1 = input('What will be your first number to operate with? ')
    try:
        float(num1)
        print(f"{Colors.Fg.yellow}", num1, f"{Colors.reset}")
        operator()
    except ValueError:
        print(f"{Colors.Fg.red}Please enter a valid number{Colors.reset} ")
        print('\n')
        first_number()


# Gets operator to be used for both numbers; ensures input is a operator
def operator():
    global opp
    opp = input('What operator will you be using on this number? ')
    if opp == '+' or opp == '-' or opp == '*' or opp == '/':
        print(f"{Colors.Fg.yellow}", opp, f"{Colors.reset}")
        second_number()
    else:
        print(f"{Colors.Fg.red}Please enter a valid operator{Colors.reset} ")
        print('\n')
        operator()


# Gets second number; ensures input is a number
def second_number():
    global num2
    num2 = input('What will be your second number? ')
    try:
        float(num2)
        print(f"{Colors.Fg.yellow}", num2, f"{Colors.reset}", '\n')
        calculate()
    except ValueError:
        print(f"{Colors.Fg.red}Please enter a valid number{Colors.reset} ")
        print('\n')
        second_number()


# Allows for user to continue using the result of their previous operation or reset and begin a new operation
def reset():
    clear = input(f"Do you wish to continue operating? {Colors.Fg.purple}Y/N{Colors.reset} ")
    if clear == 'Y' or clear == 'y':
        global num1
        num1 = result
        print(f"{Colors.Fg.yellow}", num1, f"{Colors.reset}")
        operator()
    elif clear == 'N' or clear == 'n':
        print('\n')
        first_number()
    else:
        print('Type "Y" for yes or "N" for no ')
        reset()


# Operator Logic
def calculate():
    global result

    # Addition Logic
    if opp == '+':
        result = float(num1) + float(num2)
        print(num1, opp, num2, '=', result)
        print(f"{Colors.Fg.lightBlue}Result:{Colors.reset}", f"{Colors.Fg.yellow}", result, f"{Colors.reset}", '\n')
        reset()

    # Subtraction Logic
    if opp == '-':
        result = float(num1) - float(num2)
        print(num1, opp, num2, '=', result)
        print(f"{Colors.Fg.lightBlue}Result:{Colors.reset}", f"{Colors.Fg.yellow}", result, f"{Colors.reset}", '\n')
        reset()

    # Multiplication Logic
    if opp == '*':
        result = float(num1) * float(num2)
        print(num1, opp, num2, '=', result)
        print(f"{Colors.Fg.lightBlue}Result:{Colors.reset}", f"{Colors.Fg.yellow}", result, f"{Colors.reset}", '\n')
        reset()

    # Division Logic
    if opp == '/':
        result = float(num1) / float(num2)
        print(num1, opp, num2, '=', result)
        print(f"{Colors.Fg.lightBlue}Result:{Colors.reset}", f"{Colors.Fg.yellow}", result, f"{Colors.reset}", '\n')
        reset()



print("No it's not on, evidently")
first_number()
