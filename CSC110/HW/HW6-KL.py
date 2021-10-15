data = 0
line = 0
infile = 0
cars = 0

option = int(input('Would you like to buy a car(1) or update the inventory(2)? '))

if option == 1:
    price_range = int(input('Max price: '))
    cars_in_range = []


    def read_file():
        global data
        global line
        global infile
        infile = open("Automobile_data.csv", "r")
        line = open("Automobile_data.csv", "r")
        data = infile.readline()
        while data != '':
            try:
                global cars
                data = infile.readline()
                cars = data.split(',')
                try:
                    price = int(cars[len(cars) - 1])
                except ValueError:
                    pass
                if price < price_range:
                    cars_in_range.append(cars)
            except StopIteration:
                break
    read_file()

    if cars_in_range != []:
        print('Cars that are in your price range:')
        file = open("Automobile_data.csv", "r")
        first_line = file.readline()

        print(first_line, end='')
        for i in range(len(cars_in_range)):
            if cars_in_range[i] != ['']:
                print(cars_in_range[i])

        print()
        selected_car = input("What car would you like to buy (Enter the car's index or type EXIT to quit "
                             "the program): ")

        if selected_car != 'EXIT':
            for i in range(len(cars_in_range)):
                if int(cars_in_range[i][0]) == int(selected_car):
                    print('You have selected:')
                    print(cars_in_range[i])
                    print('Thank you for shopping!')
                    infile = open("Automobile_data.csv", "r")
                    car_list = file.readlines()
                    new_data = infile.readline()
                    car = new_data.split(',')

                    print()
                    new_file = open("Automobile_data.csv", "w")
                    for new_data in car_list:
                        if car != cars_in_range[i]:
                            new_file.write(','.join(car))
                            car = new_data.split(',')
                        else:
                            car = new_data.split(',')
                    new_data = infile.readline()
                    if car != cars_in_range[i]:
                        new_file.write(','.join(car))
                    break
            infile.close()
            new_file.close()
        else:
            print('Thank you for shopping!')
    else:
        print('There are no cars in your price range')
else:
    with open("Automobile_data.csv", "r") as last_index:
        for line in last_index:
            pass
        last_line = line
        last_car = last_line.split(',')
        last_car_index = last_car[0]
    last_index.close()

    inventory = open("Automobile_data.csv", "a")
    comma = ','
    added_car = str((int(last_car_index) + 1)) + comma

    company = input('Company: ')
    body_style = input('Body-style: ')
    wheel_base = input('Wheel-base: ')
    length = input('Length: ')
    engine_type = input('Engine-type: ')
    num_of_cylinders = input('Num-of-cylinders: ')
    horsepower = input('Horsepower: ')
    average_mileage = input('Average-mileage: ')
    price = input('Price: ')

    added_car = added_car + company + ',' + body_style + ',' + wheel_base + ',' + length + ',' + engine_type + ',' + num_of_cylinders + ',' + horsepower + ',' + average_mileage + ',' + price + '\n'
    inventory.write(added_car)
    inventory.close()

    updated_inventory = open("Automobile_data.csv", "r")
    inventory_list = updated_inventory.readlines()
    print(inventory_list)
    updated_inventory.close()
