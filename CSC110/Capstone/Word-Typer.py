import time
import random
text = []
correct = 0
count = 0

input('Are you ready! Once you press enter the test will begin!')
print('Type the words!')
with open("words", "r") as infile:
    words = infile.read()
    word_list = list(map(str, words.split()))

    while True:
        for i in range(10):
            new_word = word_list[random.randint(0, len(word_list) - 1)]
            text.append(new_word)
            print(new_word, end=' ')
            if i % 15 == 0 and i != 0:
                print()
        print()
        start = time.time()
        type_word = input()
        user_text = type_word.split(' ')
        end = False
        for i in range(len(user_text)):
            if user_text[i] == '1':
                end = True
            elif user_text[i] == text[i]:
                correct = correct + 1
                count = count + 1
            elif not end:
                count = count + 1
        if end:
            break

    stop = time.time()
    WPM = count / ((stop - start) / 60)
    accuracy = 100 * (correct / count)
    print('WPM:', str(round(WPM)))
    print('Accuracy:', str(round(accuracy, 2)) + '%')
