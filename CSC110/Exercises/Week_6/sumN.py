def sumN(n):
    result = 0
    for i in range(1, n + 1):
        result = result + i
    print(result)


def sumNCubes(n):
    result = 0
    for i in range(1, n + 1):
        result = result + (i**3)
    print(result)


sumN(5)
sumNCubes(5)
