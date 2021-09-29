Hw1, Hw2, Hw3, Hw4, Hw5 = eval(input("What did you get on all your HW assignments?"))
Disc1, Disc2, Disc3, Disc4, Disc5 = eval(input("What did you get on all your Discussions?"))

total_Hw = (Hw1 + Hw2 + Hw3 + Hw4 + Hw5)
total_Disc = (Disc1 + Disc2 + Disc3 + Disc4 + Disc5)

total_Hw_Grade = total_Hw + total_Disc

Quiz, Mid, Final = eval(input("What scores did you get on your quiz, midterm, and final?"))

total_score = total_Hw_Grade + (Quiz * (12.5 * 0.333)) + (Mid * (12.5 * 0.333)) + (Final * (12.5 * 0.333))

print("Your final grade is: ", total_score)

