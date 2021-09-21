# Name: Keegan Lenz
# Date: 9/18/2021
# Project Description: Calculates the amount of paint and time needed to paint given dimensions


import math


# Setup colors
class Colors:
    reset = '\033[0m'
    bold = '\033[01m'
    underline = '\033[04m'

    class Fg:
        lightRed = '\033[91m'
        yellow = '\033[93m'


# Setup variables
length_feet = 0
length_inches = 0
width_feet = 0
width_inches = 0
height_feet = 0
height_inches = 0
doors = 0
windows = 0
mould = 0
primer = 0
finish = 0


print('AREA')
print()
print('Length')


# Area input
# Length input
def get_length_feet():
    try:
        global length_feet
        length_feet = float(input('Feet: '))
        get_length_inches()
    except ValueError:
        print()
        print(f'{Colors.Fg.lightRed}Please enter a valid input!{Colors.reset} ')
        get_length_feet()


def get_length_inches():
    try:
        global length_inches
        length_inches = float(input('Inches: '))
        print()
        print('Width')
        get_width_feet()
    except ValueError:
        print(f'{Colors.Fg.lightRed}Please enter a valid input!{Colors.reset} ')
        get_length_inches()


# Width input
def get_width_feet():
    try:
        global width_feet
        width_feet = float(input('Feet: '))
        get_width_inches()
    except ValueError:
        print(f'{Colors.Fg.lightRed}Please enter a valid input!{Colors.reset} ')
        get_width_feet()


def get_width_inches():
    try:
        global width_inches
        width_inches = float(input('Inches: '))
        print()
        print('Height')
        get_height_feet()
    except ValueError:
        print(f'{Colors.Fg.lightRed}Please enter a valid input!{Colors.reset} ')
        get_width_inches()


# Height input
def get_height_feet():
    try:
        global height_feet
        height_feet = float(input('Feet: '))
        get_height_inches()
    except ValueError:
        print(f'{Colors.Fg.lightRed}Please enter a valid input!{Colors.reset} ')
        get_height_feet()


def get_height_inches():
    try:
        global height_inches
        height_inches = float(input('Inches: '))
        print()
        print('NUMBER OF DOORS AND WINDOWS')
        get_doors()
    except ValueError:
        print(f'{Colors.Fg.lightRed}Please enter a valid input!{Colors.reset} ')
        get_height_inches()


# Doors and windows input
def get_doors():
    try:
        global doors
        doors = float(input('Doors: '))
        get_windows()
    except TypeError:
        print(f'{Colors.Fg.lightRed}Please enter a valid input!{Colors.reset} ')
        get_doors()


def get_windows():
    try:
        global windows
        windows = float(input('Windows: '))
        print()
        print('MOULDING')
        print('Width')
        get_moulding()
    except TypeError:
        print(f'{Colors.Fg.lightRed}Please enter a valid input!{Colors.reset} ')
        get_windows()


def get_moulding():
    try:
        global mould
        mould = float(input('Inches: '))
        print()
        print('PAINT COVERAGE')
        get_primer()
    except TypeError:
        print(f'{Colors.Fg.lightRed}Please enter a valid input!{Colors.reset} ')
        get_moulding()


# Paint input
def get_primer():
    try:
        global primer
        primer = float(input('Primer Square Feet per Gallon: '))
        if primer > 0:
            get_finish()
        else:
            print()
            print(f'{Colors.Fg.lightRed}This number must be greater than zero!{Colors.reset}')
            get_primer()
    except TypeError:
        print(f'{Colors.Fg.lightRed}Please enter a valid input!{Colors.reset} ')
        get_primer()


def get_finish():
    try:
        global finish
        finish = float(input('Finish Square Feet per Gallon: '))
        if finish <= 0:
            print()
            print(f'{Colors.Fg.lightRed}This number must be greater than zero!{Colors.reset}')
            get_finish()
    except TypeError:
        print(f'{Colors.Fg.lightRed}Please enter a valid input!{Colors.reset} ')
        get_finish()


# Initial function call
get_length_feet()

# Wall paint estimate
length = length_feet + (length_inches / 12)
width = width_feet + (width_inches / 12)
height = height_feet + (height_inches / 12)

wall_primer = (((length + width) * height) - (doors * 8.33) - (windows * 7.5)) / (primer * 0.5)
wall_finish = (((length + width) * height) - (doors * 8.33) - (windows * 7.5)) / (finish * 0.5)

# Wall labor estimate
wall_primer_labor = (((length + width) * height) - (doors * 8.33) - (windows * 7.5)) * 0.004
wall_finish_labor = (((length + width) * height) - (doors * 8.33) - (windows * 7.5)) * 0.006


# Ceiling paint estimate
ceil_primer = (length * width) / primer
ceil_finish = (length * width) / finish

# Ceiling labor estimate
ceil_primer_labor = (length * width) * 0.004
ceil_finish_labor = (length * width) * 0.005


# Doors and windows paint estimate
door_primer = (doors / primer) * 16.7
door_finish = (doors / finish) * 16.7
window_primer = (windows / primer) * 5
window_finish = (windows / finish) * 5

door_window_primer = door_primer + window_primer
door_window_finish = door_finish + window_finish

# Doors and windows paint estimate
door_labor = doors * 0.4
window_labor = windows * 0.225


# Moulding paint estimate
mould_primer = ((((length + width) * mould) / primer) / 6) + ((doors * 2.555) + (windows * 1.25))
mould_finish = ((((length + width) * mould) / finish) / 6) + ((doors * 2.555) + (windows * 1.25))

# Moulding labor estimate
mould_labor = ((length + width) * 0.016) + ((doors * 0.25) + (windows * 0.12))


# Output
print()
print()
print(f'{Colors.underline}', 'WALLS:', f'{Colors.reset}')
print('This job requires', f'{Colors.Fg.yellow}', round(wall_primer, 1), f'{Colors.reset}',
      'gallons of primer (estimated labor:', round(wall_primer_labor, 1), 'hours) and',
      f'{Colors.Fg.yellow}', round(wall_finish, 1), f'{Colors.reset}', 'gallons of finish (estimated labor:',
      round(wall_finish_labor, 1), 'hours).')
print()


print(f'{Colors.underline}', 'CEILING:', f'{Colors.reset}')
print('This job requires', f'{Colors.Fg.yellow}', round(ceil_primer, 1), f'{Colors.reset}',
      'gallons of primer (estimated labor:', round(ceil_primer_labor, 1), 'hours) and',
      f'{Colors.Fg.yellow}', round(ceil_finish, 1), f'{Colors.reset}', 'gallons of finish (estimated labor:',
      round(ceil_finish_labor, 1), 'hours).')
print()


print(f'{Colors.underline}', 'DOORS AND WINDOWS:', f'{Colors.reset}')
print('This job requires', f'{Colors.Fg.yellow}', round(door_window_primer, 1), f'{Colors.reset}',
      'gallons of primer and', f'{Colors.Fg.yellow}', round(door_window_finish, 1), f'{Colors.reset}',
      'gallons of finish (estimated labor for doors:', round(door_labor, 1), 'hours; estimated labor for windows:',
      round(window_labor, 1), 'hours).')
print()


print(f'{Colors.underline}', 'MOULDING:', f'{Colors.reset}')
print('This job requires', f'{Colors.Fg.yellow}', round(mould_primer, 1), f'{Colors.reset}', 'gallons of primer and',
      f'{Colors.Fg.yellow}', round(mould_finish, 1), f'{Colors.reset}', 'gallons of finish; estimated labor:',
      round(mould_labor, 2))
