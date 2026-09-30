"""AI Tic-Tac-Toe: an unbeatable opponent built with the Minimax algorithm.

Run:  python tictactoe.py
You play X, the AI plays O. Enter a number 1-9 to place your mark.
"""
import math

WIN_LINES = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
             (0, 3, 6), (1, 4, 7), (2, 5, 8),
             (0, 4, 8), (2, 4, 6)]
HUMAN, AI = "X", "O"


def winner(board):
    """Return 'X' or 'O' if someone has three in a row, else None."""
    for a, b, c in WIN_LINES:
        if board[a] != " " and board[a] == board[b] == board[c]:
            return board[a]
    return None


def minimax(board, ai_turn, depth=0):
    """Recursive game-tree search.

    Scores: AI win = 10 - depth (faster wins score higher),
            human win = depth - 10 (slower losses score higher), draw = 0.
    """
    w = winner(board)
    if w == AI:
        return 10 - depth
    if w == HUMAN:
        return depth - 10
    if " " not in board:
        return 0

    scores = []
    for i in range(9):
        if board[i] == " ":
            board[i] = AI if ai_turn else HUMAN
            scores.append(minimax(board, not ai_turn, depth + 1))
            board[i] = " "
    return max(scores) if ai_turn else min(scores)


def best_move(board):
    """Pick the square with the highest Minimax score for the AI."""
    best_score, move = -math.inf, None
    for i in range(9):
        if board[i] == " ":
            board[i] = AI
            score = minimax(board, False, 1)
            board[i] = " "
            if score > best_score:
                best_score, move = score, i
    return move


def show(board):
    cells = [c if c != " " else str(i + 1) for i, c in enumerate(board)]
    print(f"\n {cells[0]} | {cells[1]} | {cells[2]}\n---+---+---"
          f"\n {cells[3]} | {cells[4]} | {cells[5]}\n---+---+---"
          f"\n {cells[6]} | {cells[7]} | {cells[8]}\n")


def play():
    board = [" "] * 9
    human_turn = input("Go first? (y/n): ").strip().lower() != "n"
    show(board)
    while True:
        if human_turn:
            choice = input("Your move (1-9): ").strip()
            if not choice.isdigit() or not 1 <= int(choice) <= 9 or board[int(choice) - 1] != " ":
                print("Invalid move, try again.")
                continue
            board[int(choice) - 1] = HUMAN
        else:
            board[best_move(board)] = AI
            print("AI moves:")
        show(board)

        w = winner(board)
        if w:
            print("You win!" if w == HUMAN else "AI wins!")
            return
        if " " not in board:
            print("It's a draw.")
            return
        human_turn = not human_turn


if __name__ == "__main__":
    play()
