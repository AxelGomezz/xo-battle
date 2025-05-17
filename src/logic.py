# Checks winners
def diagonal_winner(board, player):
    if all(board[cell][cell] == player for cell in range(3)):
        return True
    if all(board[cell][2-cell] == player for cell in range(3)):
            return True
    return False

def vertical_winner(board, player):
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    return False

def horizontal_winner(board, player):
    if all(cell == player for cell in board[0][0:3]):
        return True
    if all(cell == player for cell in board[1][0:3]):
        return True
    if all(cell == player for cell in board[2][0:3]):
        return True
    else:
        return False
    
def check_winner(board, player): #(Main check winner function)
    if horizontal_winner(board, player) or vertical_winner(board,player) or diagonal_winner(board, player) == True:
        return True
    else:
        return False