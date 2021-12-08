price_range = int(input('Max Price: '))
print()


with open("Automobile_data.csv", "r") as infile:
    lines = infile.readlines()
    car_list = []
    for line in lines:
        cars = line.split(',')
        if cars[len(cars) - 1] != '\n':
            try:
                car_list.append(cars)
                if int(cars[len(cars) - 1]) < price_range:
                    print(cars)
            except ValueError:
                print('Available cars in your price range:')
infile.close()

print('Please type the index of the car you want:')
selected_car = input()

with open("Automobile_data.csv", "w") as infile_edit:
    for i in range(len(car_list)):
        if car_list[i][0] != selected_car:
            infile_edit.write(','.join(car_list[i]))
