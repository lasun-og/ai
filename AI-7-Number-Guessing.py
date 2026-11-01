from random import randint

number = randint(1, 100)
print("AI-7: Guess the Number")
print("Guess a number from 1 to 100.")

while True:
    guess = int(input("Your guess: "))
    if guess < number:
        print("Higher!")
    elif guess > number:
        print("Lower!")
    else:
        print("Correct!")
        break
