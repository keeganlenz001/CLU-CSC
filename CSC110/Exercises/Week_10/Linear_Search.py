with open("RandomCharacters.csv", "r") as infile:
    number = infile.readlines()
    character = []
    for i in range(len(number) - 1):
        character.append(number[i].split(',')[1].rstrip('\n'))


    def search(char):
        for j in range(len(character) - 1):
            for k in range(len(char)):
                if character[j] == char[k]:
                    print(char[k], 'at', j + 1)
                    # print(j + 1)

search(['Z', 'F', 'M'])
