
# Number Guessing Agent

low = 0
high = 20
count = 0
print("Wellcome in guessing game")
print("Think of a number between 1 and 20.")


while low <= high:
    guess = (low + high) // 2
    print("My guess is:", guess)

    feedback = input(
        "Enter higher/lower/correct: "
    ).lower()

    if feedback == "correct":
        count += 1
        print("Number guessed:", guess)
        print("Total guesses:", count)
        break

    elif feedback == "higher":
        low = guess + 1
        count += 1

    elif feedback == "lower":
        high = guess - 1
        count += 1

    else:
        print("Invalid input. Try again.")
else:
    print("Inconsistent feedback!")
