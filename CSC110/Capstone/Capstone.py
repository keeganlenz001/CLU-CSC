# Name: Keegan Lenz
# Date: 12/7/2021
# Project Description: A typing test that displays words for the user to type. Once the user has completed the test,
# the program will display the user's typing speed in words per minute and the user's accuracy.

import random
import time


class Colors:
    reset = '\033[0m'
    bold = '\033[01m'
    underline = '\033[04m'

    class Fg:
        yellow = '\033[93m'
        lightBlue = '\033[94m'


word_count = 25
print()
with open("typing_words.txt", "r") as infile:
    words = infile.readlines()
    word = ''
    text = []
    user_text = []
    correct = 0

    print('Type the highlighted words (you can end the test whenever you want by pressing '
          f'{Colors.Fg.lightBlue}{Colors.bold}ENTER{Colors.reset}):')
    for i in range(word_count):
        new_word = words[random.randint(0, len(words) - 1)].strip('\n')
        text.append(new_word)
        print(f'{Colors.Fg.yellow}' + str(new_word) + f'{Colors.reset}', end=' ')
    print()
    input(f'Press {Colors.Fg.lightBlue}{Colors.bold}ENTER{Colors.reset} to start typing ')
    start = time.time()
    user_word = input()
    stop = time.time()
    for i in range(len(user_word)):
        if user_word[i] != ' ':
            word = word + user_word[i]
        else:
            user_text.append(word)
            word = ''
    user_text.append(word)
    for i in range(len(text)):
        try:
            if user_text[i] == text[i]:
                correct = correct + 1
        except IndexError:
            break

    WPM = len(user_text) / ((stop - start) / 60)
    accuracy = (correct / len(user_text)) * 100
    print()
    print('WPM:', str(round(WPM)))
    print('Accuracy:', str(round(accuracy, 2)) + '%')
