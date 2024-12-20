from tabnanny import check

board = [[" ", " ", " "],
         [" ", " ", " "],
         [" ", " ", " "]]
iterations = 0

def print_board():
    print("  1 | 2 | 3")
    i = 1
    for list in board:
        print(i, end=" ")
        for item in list:
            print(item, end=" | ")
        print("")
        i+=1


def request_movement():
    print("\nWhat is your next movement?")
    while True:
        try:
            row = int(input("Enter row of your selection: "))
            column = int(input("Enter column of your selection: "))
        except ValueError:
            print("\nERROR: Invalid value\nPlease enter a number of position in board.")
        if board[row-1][column-1] == " ":
            return row, column
            break
        else:
            print("\nThat position in board is not empty\nPlease enter a position empty in board\n")
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
    vertical_winner(board, player)
    horizontal_winner(board, player)
    diagonal_winner(board, player)
    if horizontal_winner(board, player) or vertical_winner(board,"X") or diagonal_winner(board, "X") == True:
        return True
    else:
        return False


#MAIN
last_movement = "O"

while iterations != 9:
    print_board()
    row, column = request_movement()

    if last_movement == "O":
        do_movement(row,column,"X")
        check_winner(board, "X")

        if check_winner(board, "X") == True:
            print_board()
            print("Gamer X are the winner!")
            break

        last_movement = "X"
        iterations += 1
    else:
        do_movement(row, column, "O")
        check_winner(board, "O")

        if check_winner(board, "O") == True:
            print_board()
            print("Gamer O are the winner!")
            break

        last_movement = "O"
        iterations +=1

if iterations == 9:
    print_board()
    print("-- EMPATE --")