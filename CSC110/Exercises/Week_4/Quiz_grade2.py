grade = float(input('What grade on a 0 through 100 scale did you get your quiz? '))

if grade >= 90:
    print('You got an A!')
elif grade >= 80:
    print('You got a B!')
elif grade >= 70:
    print('You got a C')
elif grade >= 60:
    print('You got a D :(')
else:
    print("You get an F :'(")
