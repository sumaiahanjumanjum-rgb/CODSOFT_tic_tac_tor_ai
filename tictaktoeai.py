# Tic-Tac-Toe AI Game in Python

import random

board = [" " for _ in range(9)]


# Display Board
def print_board():
    print()
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("--+---+--")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("--+---+--")
    print(board[6] + " | " + board[7] + " | " + board[8])
    print()


# Check Winner
def check_winner(player):

    win_positions = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]

    for pos in win_positions:
        if board[pos[0]] == board[pos[1]] == board[pos[2]] == player:
            return True

    return False


# Check Draw
def check_draw():
    return " " not in board


# Player Move
def player_move():

    while True:

        move = int(input("Enter position (1-9): ")) - 1

        if 0 <= move <= 8 and board[move] == " ":
            board[move] = "X"
            break

        else:
            print("Invalid move. Try again.")


# AI Move
def ai_move():

    empty_positions = []

    for i in range(9):
        if board[i] == " ":
            empty_positions.append(i)

    move = random.choice(empty_positions)

    board[move] = "O"

    print("AI chose position:", move + 1)


# Main Game
print("🎮 TIC-TAC-TOE AI")
print("You = X | AI = O")

while True:

    print_board()

    # Player Turn
    player_move()

    if check_winner("X"):
        print_board()
        print("🎉 You Win!")
        break

    if check_draw():
        print_board()
        print("🤝 Draw Game!")
        break

    # AI Turn
    ai_move()

    if check_winner("O"):
        print_board()
        print("🤖 AI Wins!")
        break

    if check_draw():
        print_board()
        print("🤝 Draw Game!")
        break