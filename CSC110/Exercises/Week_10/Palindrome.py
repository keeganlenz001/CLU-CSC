def palindrome(word):
    reverse = ''
    for i in range(len(word)):
        reverse = reverse + word[len(word) - i - 1]

    if word == reverse:
        print('true')
    else:
        print('false')


palindrome('bag')
