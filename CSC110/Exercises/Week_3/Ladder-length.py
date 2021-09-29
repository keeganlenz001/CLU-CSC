import math


def main():
    height = float(input('What is the height? '))
    angle = float(input('What is the angle? '))
    radian = (math.pi / 180) * angle

    length = height / (math.sin(radian))
    print('The length of the ladder is:', length)


main()





