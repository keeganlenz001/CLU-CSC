price_range = int(input('Max price: '))
cars_in_range = []


def read_file():
    infile = open("Automobile_data.csv", "r")
    data = infile.readline()
    while data != 0:
        try:
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
    infile.close()


read_file()
print("Cars that are in your price range:")
file = open("Automobile_data.csv", "r")
first_line = file.readline()
file.close()
print(first_line, end='')
for i in range(len(cars_in_range)):
    print(cars_in_range[i])
