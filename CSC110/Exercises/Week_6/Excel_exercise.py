# price_range = float(input('Max price: '))
def read_file():
    infile = open("Automobile_data.csv", "r")
    data = infile.readlines()
    print(data)
    print(type(data))
    infile.close()


read_file()
