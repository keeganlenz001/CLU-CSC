import math

start_time = float(input('Baby sitter start time: '))
end_time = float(input('Baby sitter end time: '))

bill = 0

for i in range(int(math.floor(end_time - start_time))):
    if (end_time - i) < 9:
        bill = bill + 2.5
    else:
        bill = bill + 1.75

print('The total cost of the babysitter will be', bill, 'dollars')
print(int(math.floor(end_time - start_time)))
