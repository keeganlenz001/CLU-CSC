# Name: Keegan Lenz
# Date: 9/7/2021
# Input: Deg c
# Output: Fahrenheit


def calculate_fahrenheit():
    celsius = float(input("What temperature is it right now in celsius?  "))
    fahrenheit = (celsius * 9/5) + 32
    print(int(fahrenheit))
    calculate_fahrenheit()


calculate_fahrenheit()
