import math
def print_board(board):
    print("\n")
    for row in board:
        print("|".join(row))
        print("-" * 9)
def winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True
    return False
def full(board):
    for row in board:
        for cell in row:
            if cell not in ['X', 'O']:
                return False
    return True

def emptycells(board):
    empty = []
    for row in range(3):
        for col in range(3):
            if board[row][col] not in ['X', 'O']:
                empty.append((row, col))
    return empty

def minimax(board, depth, maximizing):
    if winner(board, 'O'):
        return 1
    elif winner(board, 'X'):
        return -1
    elif full(board):
        return 0

    if maximizing:
        best_score = -math.inf
        for row, col in emptycells(board):
            original = board[row][col]
            board[row][col] = 'O'
            score = minimax(board, depth + 1, False)
            board[row][col] = original
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for row, col in emptycells(board):
            original = board[row][col]
            board[row][col] = 'X'
            score = minimax(board, depth + 1, True)
            board[row][col] = original
            best_score = min(score, best_score)
        return best_score
def ai_move(board):
    best_score = -math.inf
    move = None
    for row, col in emptycells(board):
        original = board[row][col]
        board[row][col] = 'O'
        score = minimax(board, 0, False)
        board[row][col] = original
        if score > best_score:
            best_score = score
            move = (row, col)
    return move

# Main game function
def game_play():
    game_board = [
        ["1", "2", "3"],
        ["4", "5", "6"],
        ["7", "8", "9"],
    ]

    print("Let's start TIC-TAC-TOE")
    print("You are 'X'. AI is 'O'.")
    print_board(game_board)

    while True:
        move = input("Choose a cell (1-9): ")
        if not move.isdigit() or not (1 <= int(move) <= 9):
            print("Invalid input. Try again.")
            continue

        row = (int(move) - 1) // 3
        col = (int(move) - 1) % 3

        if game_board[row][col] in ['X', 'O']:
            print("Cell is already filled. Choose another one.")
            continue

        game_board[row][col] = 'X'
        print_board(game_board)

        if winner(game_board, 'X'):
            print("Congrats! You won the game.")
            break
        if full(game_board):
            print("It's a Draw.")
            break

        print("AI is playing..")
        ai_row, ai_col = ai_move(game_board)
        game_board[ai_row][ai_col] = 'O'
        print_board(game_board)

        if winner(game_board, 'O'):
            print("AI won the game.")
            break
        if full(game_board):
            print("It's a Draw.")
            break 
game_play()
