data = 0
infile = 0
cars = 0

price_range = int(input('Max price: '))
cars_in_range = []


def read_file():
    global data
    global infile
    infile = open("Automobile_data.csv", "r")
    data = infile.readline()
    while data != 0:
        try:
            global cars
            data = infile.readline()
            cars = data.split(',')
            try:
                price = int(cars[9])
            except ValueError:
                print()
            if price < price_range:
                cars_in_range.append(cars)
            infile.__next__()
        except StopIteration:
            break


read_file()

if cars_in_range != []:
    print('Cars that are in your price range:')
    file = open("Automobile_data.csv", "r")
    first_line = file.readline()

    print(first_line, end='')
    for i in range(len(cars_in_range)):
        print(cars_in_range[i])

    print()
    selected_car = input("What car would you like to buy (Enter the car's index or type EXIT to quit "
                         "the program): ")

    if selected_car != 'EXIT':
        for i in range(len(cars_in_range)):
            if int(cars_in_range[i][0]) == int(selected_car):
                print('You have selected:')
                print(cars_in_range[i])
                car_list = file.readlines()
                count = 0
                data = infile.readline()
                data = infile.seek(0)
                data = infile.readline()
                car = data.split(',')
                print()
                while car != cars_in_range[i]:
                    data = infile.readline()
                    car = data.split(',')
                    count += 1
                count = count - 1
                del car_list[count]
                print(car_list)
        file.close()
    else:
        print('Thank you for shopping!')
else:
    print('There are no cars in your price range')
