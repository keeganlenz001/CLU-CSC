present_val = float(input("What is the amount of money you'd like to invest? "))
interest = float(input("What is the interest rate? "))
period_num = int(input("What is the number of years? "))

for i in range(period_num + 1):
    future_val = present_val * ((1 + (interest * 0.01)) ** i)
    if i > 0:
        if i == 1:
            print(i, "year: ", future_val)
        else:
            print(i, "years: ", future_val)
print()
print("Your future investment value is: ", future_val)
