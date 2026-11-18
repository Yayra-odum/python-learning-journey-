
print("WELCOME TO THE SCORE CHECKER")

score = int(input("Enter your score (0-100): "))

if score < 0 or score > 100:
    print("Invalid score!")

elif score >= 50:
    print("Congratulations! You passed.")

else:
    print("You need more practice. Keep learning!")
