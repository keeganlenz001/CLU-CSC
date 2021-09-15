num_of_nums = int(input('How many numbers would you like to be averaged together? '))
_sum = 0
avg = 0

for i in range(num_of_nums):
    print('Please enter number', i + 1)
    num = float(input())
    _sum = _sum + num


avg = _sum / num_of_nums
print(avg)
