total = 0
pos = 0
neg = 0


def get_int():
    try:
        num = int(input('Enter an integer: '))
        global total
        total = total + num
        if num > 0:
            global pos
            pos = pos + 1
            get_int()
        elif num < 0:
            global neg
            neg = neg + 1
            get_int()
        else:
            print()
            print('# of Positive Numbers:', pos)
            print('# of Negative Numbers:', neg)
            print('Total:', total)

    except ValueError:
        print('Please enter a valid input!')
        get_int()


get_int()
