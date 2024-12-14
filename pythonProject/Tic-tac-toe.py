board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
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


def do_movement_x(row, column):
    board[row-1][column-1] = "X"


def do_movement_o(row,column):
    board[row-1][column-1] = "O"


def horizontal_winner():
    if all(cell == "X" for cell in board[0][0:3]):
        return True
    if all(cell == "X" for cell in board[1][0:3]):
        return True
    if all(cell == "X" for cell in board[2][0:3]):
        return True
    if all(cell == "O" for cell in board[0][0:3]):
        return True
    if all(cell == "O" for cell in board[1][0:3]):
        return True
    if all(cell == "O" for cell in board[2][0:3]):
        return True
    else:
        return False


#MAIN
last_movement = "O"
verify_winner = False
while iterations != 9:
    print_board()
    row, column = request_movement()

    if last_movement == "O":
        do_movement_x(row,column)
        verify_winner = horizontal_winner()
        if verify_winner == True:
            print_board()
            print("Gamer X are the winner!")
            break
        last_movement = "X"
        iterations += 1

    else:
        do_movement_o(row, column)
        verify_winner = horizontal_winner()
        if verify_winner == True:
            print_board()
            print("Gamer O are the winner!")
            break
        last_movement = "O"
        iterations +=1

#if iterations == 9:
 #   print_board()
  #  print("-- EMPATE --")