weight = float(input('Your weight in pounds: '))
height = float(input('Your height in inches: '))

bmi = (weight * 720) / (height ** 2)

print(bmi)

if bmi < 19:
    print('Your BMI is below the healthy range')
elif bmi < 25:
    print('Your BMI is in the healthy range!')
else:
    print('Your BMI is above the healthy range')
