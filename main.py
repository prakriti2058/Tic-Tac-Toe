import threading
import random
import time

board = [' ' for _ in range(9)]
lock = threading.Lock()
game_over = False

def print_board():
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")
    print()

def check_winner(player):
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
                      (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
                      (0, 4, 8), (2, 4, 6)]             # Diagonals
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False

def is_draw():
    return ' ' not in board

def player_move(player):
    global game_over
    while not game_over:
        with lock:
            # Choose a random empty spot on the board
            available_moves = [i for i in range(9) if board[i] == ' ']
            if available_moves:
                move = random.choice(available_moves)
                board[move] = player
                print(f"Player {player} makes a move:")
                print_board()
                
                if check_winner(player):
                    print(f"Player {player} wins!")
                    game_over = True
                    return
                
                if is_draw():
                    print("It's a draw!")
                    game_over = True
                    return

        time.sleep(random.uniform(0.5, 1.5))

player_x_thread = threading.Thread(target=player_move, args=('X',))
player_o_thread = threading.Thread(target=player_move, args=('O',))

print("Starting the Tic-Tac-Toe game!")
print_board()

player_x_thread.start()
player_o_thread.start()

player_x_thread.join()
player_o_thread.join()

print("Game over!")
