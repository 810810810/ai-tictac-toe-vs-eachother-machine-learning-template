import argparse
import time
from tic_tac_toe_ai import TicTacToeAI

def play_tic_tac_toe(ai1, ai2):
    board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    current_player = 'X'
    while True:
        if current_player == 'X':
            row, col = ai1.get_move(str(board))
        else:
            row, col = ai2.get_move(str(board))
        if board[row][col] == ' ':
            board[row][col] = current_player
        winner = get_winner(board)
        if winner:
            if winner == 'X':
                ai1.learn(str(board), row * 3 + col, 1, str(board))
                ai2.learn(str(board), row * 3 + col, -1, str(board))
            else:
                ai1.learn(str(board), row * 3 + col, -1, str(board))
                ai2.learn(str(board), row * 3 + col, 1, str(board))
            print_board(board)
            print(f"{winner} wins!")
            break
        elif is_full(board):
            ai1.learn(str(board), row * 3 + col, 0, str(board))
            ai2.learn(str(board), row * 3 + col, 0, str(board))
            print_board(board)
            print("It's a tie!")
            break
        else:
            if current_player == 'X':
                ai1.learn(str(board), row * 3 + col, 0, str(board))
                current_player = 'O'
            else:
                ai2.learn(str(board), row * 3 + col, 0, str(board))
                current_player = 'X'

def get_winner(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != ' ':
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != ' ':
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[0][2]
    return None

def is_full(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                return False
    return True

def print_board(board):
    for row in board:
        print(row)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--config', default='config.ini', help='Path to config file')
    parser.add_argument('--delay', type=float, default=1.0, help='Delay between games')
    args = parser.parse_args()

    ai1 = TicTacToeAI('X', args.config)
    ai2 = TicTacToeAI('O', args.config)

    while True:
        play_tic_tac_toe(ai1, ai2)
        time.sleep(args.delay)
