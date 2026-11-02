coins = [8, 15, 3, 7, 12, 15, 4, 8, 10]

ai_score = 0
human_score = 0


def minimax(coins, left, right, player):

    if left > right:
        return 0

    if player == 1:  # AI turn (MAX)

        take_left = coins[left] + minimax(
            coins, left + 1, right, 0
        )

        take_right = coins[right] + minimax(
            coins, left, right - 1, 0
        )

        return max(take_left, take_right)

    else:  # Human turn (MIN)

        take_left = -coins[left] + minimax(
            coins, left + 1, right, 1
        )

        take_right = -coins[right] + minimax(
            coins, left, right - 1, 1
        )

        return min(take_left, take_right)


def get_best_move(left, right):

    left_value = coins[left] + minimax(
        coins, left + 1, right, 0
    )

    right_value = coins[right] + minimax(
        coins, left, right - 1, 0
    )

    if left_value >= right_value:
        return "L"
    else:
        return "R"


print("AI Coin Game using Minimax")
print("Coins:", coins)

left = 0
right = len(coins) - 1

while left <= right:

    # AI turn
    move = get_best_move(left, right)

    if move == "L":
        coin = coins[left]
        left += 1
        print("AI takes left coin:", coin)

    else:
        coin = coins[right]
        right -= 1
        print("AI takes right coin:", coin)

    ai_score += coin

    if left > right:
        break

    # Human turn
    print("Remaining coins:", coins[left:right + 1])

    while True:

        choice = input(
            "Choose L for left or R for right: "
        ).upper()

        if choice == "L":
            coin = coins[left]
            left += 1
            break

        elif choice == "R":
            coin = coins[right]
            right -= 1
            break

        else:
            print("Invalid choice! Enter L or R.")

    human_score += coin
    print("You took:", coin)


print("\nFinal Scores")
print("AI Score:", ai_score)
print("Human Score:", human_score)

if ai_score > human_score:
    print("AI Wins!")

elif human_score > ai_score:
    print("Human Wins!")

else:
    print("Draw!")
