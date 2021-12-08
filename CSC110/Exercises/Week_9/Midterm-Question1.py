def reverse_text():
    user_text = input('Line of text (type Done, done, or d to exit the program): ')
    reversed_word = ''
    while user_text != 'Done' or user_text != 'done' or user_text != 'd':
        for i in range(len(user_text)):
            reversed_word = reversed_word + user_text[len(user_text) - i - 1]
        print(reversed_word)
        reversed_word = ''
        user_text = input('Line of text (type Done, done, or d to exit the program): ')


reverse_text()
