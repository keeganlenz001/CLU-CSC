# Name: Keegan Lenz
# Date: 9/18/2021
# Project Description: Calculates the amount of paint and time needed to paint given dimensions


import math

# dimension input
length = float(input('Length: '))
width = float(input('Width: '))
height = float(input('Height: '))
doors = float(input('Number of Doors: '))
windows = float(input('Number of Windows: '))

# paint input
primer = float(input('Primer Square Feet per Gallon: '))
finish = float(input('Finish Square Feet per Gallon: '))


# wall paint estimate
wall_primer = (((length + width) * height) - (doors * 8.33) - (windows * 7.5)) / (primer * 0.5)
wall_finish = (((length + width) * height) - (doors * 8.33) - (windows * 7.5)) / (finish * 0.5)

# wall labor estimate
wall_primer_labor = (((length + width) * height) - (doors * 8.33) - (windows * 7.5)) * 0.004
wall_finish_labor = (((length + width) * height) - (doors * 8.33) - (windows * 7.5)) * 0.006


# ceiling paint estimate
ceil_primer = (length * width) / primer
ceil_finish = (length * width) / finish

# ceiling labor estimate
ceil_primer_labor = (length * width) * 0.004
ceil_finish_labor = (length * width) * 0.005


# doors and windows paint estimate
door_primer = (doors / primer) * 16.7
door_finish = (doors / finish) * 16.7
window_primer = (windows / primer) * 5
window_finish = (windows / finish) * 5

door_window_primer = door_primer + window_primer
door_window_finish = door_finish + window_finish

# doors and windows paint estimate
door_labor = doors * 0.4
window_labor = windows * 0.225


# moulding paint estimate


print()
print('WALLS:')
print('This job requires', round(wall_primer, 1), 'gallons of primer (estimated labor:', round(wall_primer_labor, 1),
      'hours) and', round(wall_finish, 1), 'gallons of finish (estimated labor:', round(wall_finish_labor, 1),
      'hours).')
print()


print('CEILING:')
print('This job requires', round(ceil_primer, 1), 'gallons of primer (estimated labor:', round(ceil_primer_labor, 1),
      'hours) and', round(ceil_finish, 1), 'gallons of finish (estimated labor:', round(ceil_finish_labor, 1),
      'hours).')
print()


print('DOORS AND WINDOWS:')
print('This job requires', round(door_window_primer, 1), 'gallons of primer and', round(door_window_finish, 1),
      'gallons of finish (estimated labor for doors:', round(door_labor, 1), 'hours; estimated labor for windows:',
      round(window_labor, 1), 'hours).')
print()


# print('MOULDING')


