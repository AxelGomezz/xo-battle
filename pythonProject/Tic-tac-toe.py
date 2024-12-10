board = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]

def print_board():
    for list in board:
        for item in list:
            print(item, end=" | ")
        print("\n")

print_board()

