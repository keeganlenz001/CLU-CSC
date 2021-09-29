num_of_nums = int(input('How many numbers would you like to be summed? '))
result = 0

for i in range(num_of_nums):
    print('Please enter number', i + 1)
    num = float(input())
    result = result + num

print(result)
