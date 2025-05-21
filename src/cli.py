def print_board(board):
    print("  1 | 2 | 3")
    i = 1
    for list in board:
        print(i, end=" ")
        for item in list:
            print(item, end=" | ")
        print("")
        i+=1


def request_movement(board):
    print("\nWhat's your next move?")
    while True:
        try:
            row = int(input("Enter row of your selection: "))
            column = int(input("Enter column of your selection: "))

            if row in [1,2,3] and column in [1,2,3]:
                return row, column
                break
            else:
                print("\nERROR: POSITION SELECTED IS INVALID.\n")
                print_board(board)

        except ValueError:
            print("\nERROR: INVALID VALUE\nPlease enter a number of position in board.")
            print_board(board)        