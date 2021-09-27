speed_limit = int(input('Speed limit in mph: '))
speed = int(input('How fast were you going in mph? '))

fine = 0

if speed > speed_limit:
    fine = fine + 50
    amount_over = 5 * (speed - speed_limit)
    fine = fine + amount_over
    if speed > 90:
        fine = fine + 200
    print('Your total fine is:', fine, 'dollars')
else:
    print('You were under the speed limit')
