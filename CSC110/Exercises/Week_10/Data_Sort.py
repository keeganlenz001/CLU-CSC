with open("HistoricalData_1636073927660.csv", "r") as infile:
    data = infile.readlines()
    split_data = []
    low_data = []
    for i in range(len(data)):
        split_data.append(data[i].split(','))

    for i in range(len(split_data)):
        low_data.append(split_data[i][len(split_data[i]) - 1].strip('$'))

    print(low_data)



