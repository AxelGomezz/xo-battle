
def print_board(board):
    print("  1 | 2 | 3")
    i = 1
    for list in board:
        print(i, end=" ")
        for item in list:
            print(item, end=" | ")
        print("")
        i+=1