board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

def print_board():
    print("column\n  1 | 2 | 3")
    i = 1
    for list in board:
        print(i, end=" ")
        for item in list:
            print(item, end=" | ")
        print("")
        i+=1

def request_movement():
    print("\nWhat is your next moviment?")

    row = int(input("Enter row of your selection: "))
    column = int(input("Enter column of your selection"))
    return row, column

def do_movement_x(row, column):
        board[row-1][column-1] = "X"

#MAIN
print_board()
row, column = request_movement()
do_movement_x(row, column)
print_board()


