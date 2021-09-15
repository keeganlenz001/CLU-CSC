# Keegan Lenz
# Date: 9/2/2021
# Project: Simulates large differences between small input changes
# Input: Number between 0 and 1
# Output: input * 3.9 * (input - 1)


def main():
    x = input('Enter a number between 0 and 1 ')

    try:
        x = float(x)
        if 0 < x < 1:
            for i in range(10):
                x = 3.9 * x * (1 - x)
                print(x)
            print('\n')
            main()
        else:
            print('Please enter a valid input!', '\n')
            main()
    except ValueError:
        print('Please enter a valid input!', '\n')
        main()


main()
