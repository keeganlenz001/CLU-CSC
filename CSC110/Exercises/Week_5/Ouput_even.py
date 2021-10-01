num = 100
# With array
# arr = []
length = 0

while num <= 1000:
    if num % 5 == 0 or num % 6 == 0:
        # Without array
        if length < 10:
            print(num, end=" ")
            length = length + 1
        else:
            print()
            length = 0

        # With array
        # arr.append(num)
        # length = length + 1
        # if length == 10:
        #     print(arr)
        #     arr = []
        #     length = 0
        num = num + 1
    else:
        num = num + 1
