
low = 1
high = 100

print("Think of a number between 1 and 100")

while low <= high:
    guess = (low + high) // 2

    print("My guess is:", guess)
    feedback = input("Enter higher, lower, or correct: ")

    if feedback == "higher":
        low = guess + 1

    elif feedback == "lower":
        high = guess - 1

    elif feedback == "correct":
        print("I guessed the correct number!")
        break

    else:
        print("Invalid feedback!")
