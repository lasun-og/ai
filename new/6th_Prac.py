
from functools import lru_cache

# Take coin values from the user
coins = list(map(int, input(
    "Enter coin values separated by spaces: "
).split()))

n = len(coins)

# Minimax algorithm
@lru_cache(None)
def minimax(left, right, turn):
    if left > right:
        return 0

    if turn == 1:  # AI turn
        return max(
            coins[left] + minimax(left + 1, right, 0),
            coins[right] + minimax(left, right - 1, 0)
        )
    else:  # Human turn
        return min(
            minimax(left + 1, right, 1),
            minimax(left, right - 1, 1)
        )


# Play the game
left = 0
right = n - 1
ai_score = 0
human_score = 0
turn = 1

while left <= right:
    print("\nRemaining coins:", coins[left:right + 1])

    if turn == 1:
        left_value = coins[left] + minimax(left + 1, right, 0)
        right_value = coins[right] + minimax(left, right - 1, 0)

        if left_value >= right_value:
            chosen = coins[left]
            left += 1
            print("AI chooses left coin:", chosen)
        else:
            chosen = coins[right]
            right -= 1
            print("AI chooses right coin:", chosen)

        ai_score += chosen
        turn = 0

    else:
        choice = input("Choose left or right (L/R): ").upper()

        if choice == "L":
            chosen = coins[left]
            left += 1
        elif choice == "R":
            chosen = coins[right]
            right -= 1
        else:
            print("Invalid choice! Try again.")
            continue

        human_score += chosen
        print("You chose:", chosen)
        turn = 1

# Display final scores
print("\n===== GAME OVER =====")
print("AI Score:", ai_score)
print("Your Score:", human_score)

if ai_score > human_score:
    print("AI wins!")
elif human_score > ai_score:
    print("You win!")
else:
    print("It's a draw!")
