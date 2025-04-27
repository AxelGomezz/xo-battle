import random
board = [[" ", " ", " "],
         [" ", " ", " "],
         [" ", " ", " "]]
iterations = 0
empty_positions = []

def print_board():
    print("  1 | 2 | 3")
    i = 1
    for list in board:
        print(i, end=" ")
        for item in list:
            print(item, end=" | ")
        print("")
        i+=1


def check_empty_position(empty_positions):
    empty_positions.clear()
    for row in range(3):
        for item in range(3):
            if board[row][item] == " ":
                empty_positions.append((row,item))

def ai_move(empty_positions):
    row,column = random.choice(empty_positions)
    board[row][column] = "O" 

def request_movement():
    print("\nWhat's your next move?")
    while True:
        try:
            row = int(input("Enter row of your selection: "))
            column = int(input("Enter column of your selection: "))

            if row in [1,2,3] and column in [1,2,3]:

                if board[row - 1][column - 1] == " ":
                    return row, column
                    break
                else:
                    print("\nThat position in board is not empty\nPlease enter a position empty in board\n")
                    print_board()

            else:
                print("\nERROR: POSITION SELECTED IS INVALID.\n")
                print_board()
        except ValueError:
            print("\nERROR: INVALID VALUE\nPlease enter a number of position in board.")
            print_board()


def do_movement(row, column,player):
    board[row-1][column-1] = player


def horizontal_winner(board, player):
    if all(cell == player for cell in board[0][0:3]):
        return True
    if all(cell == player for cell in board[1][0:3]):
        return True
    if all(cell == player for cell in board[2][0:3]):
        return True
    else:
        return False

def vertical_winner(board, player):
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    return False


def diagonal_winner(board, player):
    if all(board[cell][cell] == player for cell in range(3)):
        return True
    if all(board[cell][2-cell] == player for cell in range(3)):
            return True
    return False


def check_winner(board, player):
    if horizontal_winner(board, player) or vertical_winner(board,player) or diagonal_winner(board, player) == True:
        return True
    else:
        return False


#MAIN
last_movement = "O"

while iterations != 9:
    print_board()

    if last_movement == "O":
        row, column = request_movement()
        do_movement(row, column,"X")

        if check_winner(board, "X") == True:
            print_board()
            print("Player X is the winner!")
            break

        last_movement = "X"
    else:
        check_empty_position(empty_positions)
        print("\n-- BOT O Realized move --")
        ai_move(empty_positions)
        if check_winner(board, "O") == True:
            print_board()
            print("Player O is the winner!")
            break

        last_movement = "O"
    iterations +=1

if iterations == 9:
    print_board()
    print("-- EMPATE --")