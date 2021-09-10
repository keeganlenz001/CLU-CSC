num1 = float(input("What will be your first number? "))
num2 = float(input("What will be your second number? "))
num3 = float(input("What will be your third number? "))

result = num1 + num2 + num3

if result.is_integer():
    print(int(result))
else:
    print(result)
