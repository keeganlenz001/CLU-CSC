import math


def sphere_area(radius):
    area = 4 * math.pi * radius**2
    print('Area:', area)


def sphere_volume(radius):
    volume = (4/3) * math.pi * radius**3
    print('Volume:', volume)


sphere_area(4)
sphere_volume(4)
