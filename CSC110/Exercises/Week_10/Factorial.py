n = int(input('Number: '))
result = 0

for i in range(n):
    result = result + (n * (n - i - 1))

print(result)
