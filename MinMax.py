
def minimax(board, is_max):
    if "X" in board and board.count("X") == 3:
        return 1
    if "O" in board and board.count("O") == 3:
        return -1

    if "_" not in board:
        return 0

    if is_max:
        best = -999
        for i in range(3):
            if board[i] == "_":
                board[i] = "X"
                best = max(best, minimax(board, False))
                board[i] = "_"
        return best

    else:
        best = 999
        for i in range(3):
            if board[i] == "_":
                board[i] = "O"
                best = min(best, minimax(board, True))
                board[i] = "_"
        return best


board = ["X", "O", "_"]

best_score = -999
best_move = -1

for i in range(3):
    if board[i] == "_":
        board[i] = "X"
        score = minimax(board, False)
        board[i] = "_"

        if score > best_score:
            best_score = score
            best_move = i

board[best_move] = "X"

print("Best Move:", best_move)
print("Final Board:", board)
