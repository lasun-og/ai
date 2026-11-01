print("AI-7: Guess the Number")
print("Think of a number from 1 to 100.")
print("Tell the agent: higher, lower, or correct.")

low = 1
high = 100

while low <= high:
    guess = (low + high) // 2
    print("Is your number", guess, "?")
    answer = input("Your answer: ").lower()

    if answer == "higher":
        low = guess + 1
    elif answer == "lower":
        high = guess - 1
    elif answer == "correct":
        print("The agent guessed your number!")
        break
    else:
        print("Please enter higher, lower, or correct.")

if low > high:
    print("Your answers did not match a number from 1 to 100.")
