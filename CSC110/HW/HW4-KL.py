# Name: Keegan Lenz
# Date: 9/23/2021
# Project Description: Tells if a fraction is proper or improper. If the fraction is improper, it shows the fraction
# simplified

num = 0
denom = 0


def get_numberator():
    try:
        global num
        num = int(input('Enter a numerator: '))
        get_denominator()
    except ValueError:
        print('Please enter a valid input!')
        get_numberator()


def get_denominator():
    try:
        global denom
        denom = int(input('Enter a denominator: '))
        calculate()
    except ValueError:
        print('Please enter a valid input!')
        get_denominator()


def calculate():
    remainder = num % denom

    if num < denom:
        print(num, '/', denom, 'is a proper fraction')
    else:
        if remainder == 0:
            print(num, '/', denom, 'is an improper fraction and can be reduced to', num // denom)
        else:
            print(num, '/', denom, 'is an improper fraction and its mixed fraction is',
                  (num - remainder) // denom, '+', remainder, '/', denom)


get_numberator()
