import random
from logic import check_winner, verify_move, do_movement, switch_turn
from cli import print_board, request_movement
from ai import check_empty_position, ai_move

board = [[" ", " ", " "],
         [" ", " ", " "],
         [" ", " ", " "]]

iterations = 0
empty_positions = []


# // MAIN //
current_turn = "O"
move = ()

while iterations != 9:
    print_board(board)

    current_turn = switch_turn(current_turn) 
    if current_turn == "X":
        
        while True:
            row, column = request_movement(board)
            move = verify_move(board, row, column)
            if move is not None:
                row, column = move
                do_movement(board, row, column,"X")
                break
        
        if check_winner(board, "X") == True:
            print_board(board)
            print("Player X is the winner!")
            break

    else:
        check_empty_position(empty_positions, board)
        print("\n-- BOT O Realized move --")
        ai_move(empty_positions, board)
        if check_winner(board, "O") == True:
            print_board(board)
            print("Player O is the winner!")
            break

    iterations +=1

if iterations == 9:
    print_board(board)
    print("-- EMPATE --")