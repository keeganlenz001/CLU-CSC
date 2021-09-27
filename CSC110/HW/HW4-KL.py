# Name: Keegan Lenz
# Date: 9/23/2021
# Project Description: Tells if a fraction is proper or improper. If the fraction is improper, it shows the fraction
# simplified

num = int(input('Enter a numerator: '))
denom = int(input('Enter a denominator: '))

remainder = num % denom

if num < denom:
    print(num, '/', denom, 'is a proper fraction')
else:
    if remainder == 0:
        print(num, '/', denom, 'is an improper fraction and can be reduced to', num // denom)
    else:
        print(num, '/', denom, 'is an improper fraction and its mixed fraction is',
              (num - remainder) // denom, '+', remainder, '/', denom)
