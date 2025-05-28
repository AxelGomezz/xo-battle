import random

#       // AI //
def ai_move(empty_positions, board):
    counter_play, verify_counter_play = find_critical_moves(board, player = "X")
    winning_move, verify_winning_move = find_winning_moves(board, player = "O")
    key_move, verify_key_move = verify_key_moves(board)
    if verify_winning_move == True:
        row, column = winning_move
        board[row][column] = "O"
    elif verify_counter_play == True:
        row, column = counter_play
        board[row][column] = "O"
    elif verify_key_move == True:
        row, column = key_move
        board[row][column] = "O"
    else:
        row,column = random.choice(empty_positions)
        board[row][column] = "O" 

def check_empty_position(empty_positions, board):
    empty_positions.clear()
    for row in range(3):
        for item in range(3):
            if board[row][item] == " ":
                empty_positions.append((row,item))

def verify_key_moves(board):
    key_move = None
    if board[1][1] == " ":
        key_move = 1, 1
        return key_move, True
    
    elif board[0][0] == " ":
        key_move = 0, 0
        return key_move, True
    
    elif board[0][2] == " ":
        key_move = 0, 2
        return key_move, True
    
    elif board[2][0] == " ":
        key_move = 2, 0
        return key_move, True
    
    elif board[2][2] == " ":
        key_move = 2, 2
        return key_move, True
    
    else:
        return None, False

# - Find winnings moves - 
def find_winning_moves(board, player): # (Main winning moves function)
    winning_play, verify_winning_play = find_diagonal_critical_moves(board, player)
    if verify_winning_play == True:
        return winning_play, True
    
    winning_play, verify_winning_play = find_horizontal_critical_moves(board, player)
    if verify_winning_play == True:
        return winning_play, True
    
    winning_play, verify_winning_play = find_vertical_critical_moves(board, player)
    if verify_winning_play == True:
        return winning_play, True
    
    return None, False

def find_vertical_winning_move(board, player):
    for col in range(3):
        count = 0
        winning_move = None
        for row in range(3):
            if board[row][col] == player:
                count += 1
            elif board[row][col] == " ":
                winning_move = row, col
        if count == 2 and winning_move is not None:
            return winning_move, True
    return None, False

def find_horizontal_winning_move(board, player):
    for index_row, row in enumerate(board):
        count = 0
        winning_move = None
        for index_col, cell in enumerate(row):
            if  cell == player:
                count += 1
            elif cell == " ":
                winning_move = index_col
        if count == 2 and winning_move is not None:
            return (index_row, winning_move), True
    return None, False

def find_diagonal_winning_move(board, player):
    count = 0
    winning_move = None

    for index in range(3): #check first diagonal
        if board[index][index] == player:
            count += 1
        elif board[index][index] == " ":
            winning_move = index, index
    if count == 2 and winning_move is not None:
        return winning_move, True

#Reset variables values
    count = 0 
    winning_move = None

    for index in range(3):# check second diagonal
        if board[index][2-index] == player:
            count += 1
        elif board[index][2-index] == " ":
            winning_move = index, 2-index
    if count == 2 and winning_move is not None:
        return winning_move, True
    
    return None, False

# - find critical moves - 
def find_critical_moves(board, player): #(Main critical moves function)
    counter_play, verify_counter_play = find_diagonal_critical_moves(board, player = "X")
    if verify_counter_play == True:
        return counter_play, True
    
    counter_play, verify_counter_play = find_horizontal_critical_moves(board, player = "X")
    if verify_counter_play == True:
        return counter_play, True
    
    counter_play, verify_counter_play = find_vertical_critical_moves(board, player = "X")
    if verify_counter_play == True:
        return counter_play, True
    
    return None, False

def find_vertical_critical_moves(board, player):
    for col in range(3):
        count = 0
        danger_position = None
        for row in range(3):
            if board[row][col] == player:
                count += 1
            elif board[row][col] == " ":
                danger_position = row, col
        if count == 2 and danger_position is not None:
            return danger_position, True
    return None, False

def find_diagonal_critical_moves(board, player):
    count = 0
    danger_position = None

    for index in range(3): #check first diagonal
        if board[index][index] == player:
            count += 1
        elif board[index][index] == " ":
            danger_position = index, index
    if count == 2 and danger_position is not None:
        return danger_position, True

#Reset variables values
    count = 0 
    danger_position = None

    for index in range(3):# check second diagonal
        if board[index][2-index] == player:
            count += 1
        elif board[index][2-index] == " ":
            danger_position = index, 2-index
    if count == 2 and danger_position is not None:
        return danger_position, True
    
    return None, False

def find_horizontal_critical_moves(board, player):
    for index_row, row in enumerate(board):
        count = 0
        danger_position = None
        for index_col, cell in enumerate(row):
            if  cell == player:
                count += 1
            elif cell == " ":
                danger_position = index_col
        if count == 2 and danger_position is not None:
            return (index_row, danger_position), True
    return None, False
