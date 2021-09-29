def main():
    print('Change counter')
    print()
    print('Please enter the count of each coin type.')
    quarters = int(input('Quarters: '))
    dimes = int(input('Dimes: '))
    nickles = int(input('Nickles: '))
    pennies = int(input('Pennies: '))
    total = (quarters * .25) + (dimes * .10) + (nickles * .05) + (pennies * .01)

    print('Your total amount of money is:', total)


main()
