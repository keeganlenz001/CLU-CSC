def reverse(num):
    num_str = str(num)
    reverse_num = ''
    for i in range(len(num_str)):
        reverse_num = reverse_num + num_str[len(num_str) - i - 1]
    print(reverse_num)


user_num = input('Enter a number: ')
reverse(user_num)
