total = 0
for i in range(1, 100, 2):
    num = i
    den = num + 2
    total = total + (num / den)
    print(num, '/', den, '+', end=" ")

print()
print('Total:', total)


