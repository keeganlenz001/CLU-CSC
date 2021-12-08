fruits = ['Apple', 'Orange', 'Banana', 'Strawberry', 'Blueberry']


def search(fruit):
    for i in range(len(fruits)):
        if fruit == fruits[i]:
            print('We have what you are looking for')
            break
        else:
            print("Sorry, we don't have what you are looking for")
            break


search('Berry')
