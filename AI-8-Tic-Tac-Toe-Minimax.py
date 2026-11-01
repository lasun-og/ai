def show_board(board):
    print(board[0], "|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8])


def winner(board, mark):
    lines = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
             (0, 3, 6), (1, 4, 7), (2, 5, 8),
             (0, 4, 8), (2, 4, 6)]
    for a, b, c in lines:
        if board[a] == mark and board[b] == mark and board[c] == mark:
            return True
    return False


def minimax(board, ai_turn):
    if winner(board, "O"):
        return 1
    if winner(board, "X"):
        return -1
    if " " not in board:
        return 0

    if ai_turn:
        best_score = -2
        for place in range(9):
            if board[place] == " ":
                board[place] = "O"
                score = minimax(board, False)
                board[place] = " "
                if score > best_score:
                    best_score = score
        return best_score

    best_score = 2
    for place in range(9):
        if board[place] == " ":
            board[place] = "X"
            score = minimax(board, True)
            board[place] = " "
            if score < best_score:
                best_score = score
    return best_score


board = [" "] * 9
print("AI-8: Tic-Tac-Toe")
print("You are X. Choose a square from 1 to 9.")

while True:
    show_board(board)
    place = int(input("Your move: ")) - 1
    if place < 0 or place > 8 or board[place] != " ":
        print("Choose an empty square from 1 to 9.")
        continue
    board[place] = "X"

    if winner(board, "X"):
        show_board(board)
        print("You win!")
        break
    if " " not in board:
        show_board(board)
        print("Draw!")
        break

    best_score = -2
    best_place = 0
    for place in range(9):
        if board[place] == " ":
            board[place] = "O"
            score = minimax(board, False)
            board[place] = " "
            if score > best_score:
                best_score = score
                best_place = place
    board[best_place] = "O"
    print("AI chooses square", best_place + 1)

    if winner(board, "O"):
        show_board(board)
        print("AI wins!")
        break
    if " " not in board:
        show_board(board)
        print("Draw!")
        break
