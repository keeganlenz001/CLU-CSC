total = 0
count = 0

num = int(input('Enter a number: '))
while num != 0:
    total = total + num
    count = count + 1
    num = int(input('Enter a number: '))

print('Total:', float(total))
print('Average:', total / count)
