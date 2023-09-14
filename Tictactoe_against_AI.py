import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(3):
        if all(row[col] == player for row in board):
            return True

    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def is_board_full(board):
    return all(cell != " " for row in board for cell in row)

def get_empty_cells(board):
    empty_cells = []
    for row in range(3):
        for col in range(3):
            if board[row][col] == " ":
                empty_cells.append((row, col))
    return empty_cells

def minimax(board, depth, is_maximizing):
    if check_winner(board, "X"):
        return -1
    if check_winner(board, "O"):
        return 1
    if is_board_full(board):
        return 0

    if is_maximizing:
        best_score = -float("inf")
        for row, col in get_empty_cells(board):
            board[row][col] = "O"
            score = minimax(board, depth + 1, False)
            board[row][col] = " "
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = float("inf")
        for row, col in get_empty_cells(board):
            board[row][col] = "X"
            score = minimax(board, depth + 1, True)
            board[row][col] = " "
            best_score = min(score, best_score)
        return best_score

def get_best_move(board):
    best_move = None
    best_score = -float("inf")
    for row, col in get_empty_cells(board):
        board[row][col] = "O"
        score = minimax(board, 0, False)
        board[row][col] = " "
        if score > best_score:
            best_score = score
            best_move = (row, col)
    return best_move

def play_game(): 
    board = [[" " for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while True:
        player_row, player_col = map(int, input("Enter your move (row and column): ").split())
        if board[player_row][player_col] == " ":
            board[player_row][player_col] = "X"
        else:
            print("Invalid move. Try again.")
            continue

        print_board(board)

        if check_winner(board, "X"):
            print("You win!")
            break

        if is_board_full(board):
            print("It's a tie!")
            break

        print("Computer's turn...")
        computer_row, computer_col = get_best_move(board)
        board[computer_row][computer_col] = "O"
        print_board(board)

        if check_winner(board, "O"):
            print("Computer wins!")
            break

        if is_board_full(board):
            print("It's a tie!")
            break

if __name__ == "__main__":
    play_game()
