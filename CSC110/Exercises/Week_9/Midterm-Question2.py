weight = float(input('Weight in pounds: '))
height = float(input('Height in inches: '))

BMI = (weight * 720) / (height ** 2)
print(BMI)

if BMI < 19:
    print('Your BMI is below the healthy range')
elif BMI < 25:
    print('Your BMI is within the healthy range')
else:
    print('Your BMI is above the healthy range')
