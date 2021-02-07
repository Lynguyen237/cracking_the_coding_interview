# Tic Tac Win: Design an algorithm to figure out if someone has won a game of tic-tac-toe.
# Assume that there's no situation in which 2 people have won
# 3x3 board
# Return x, o, or none

# xoo
# xox
# oox #o

# xxx
# xox
# oox #x

# xox
# xox
# oxo #o


# SOLUTION - 3x3 board
            
def tic_tac_toe(row1, row2, row3):
    
    # Check for columns 
    for i in range(2): # Double check Big O
        if row1[i] == row2[i] == row3[i]:
            return row1[i]
    
    # Check for rows:
    if len(set(row1)) == 1:
        return row1[0]
    if len(set(row2)) == 1:
        return (row2[0])
    if len(set(row3)) == 1:
        return (row3[0])
    
    # Check for diagonals:
    if row1[0] == row2[1] == row3[2]:
        return row1[0]
    if row1[2] == row2[1] == row3[0]:
        return row1[2]
   
# print(tic_tac_toe(["x","o","o"],["x","o","x"], ["o","o","x"])) #o
# print(tic_tac_toe(["x","x","x"],["x","o","x"], ["o","o","x"])) #x
# print(tic_tac_toe(["x","x","o"],["x","o","x"], ["o","o","x"])) #o
# print(tic_tac_toe(["x","o","x"],["x","o","x"], ["o","x","o"])) #none



# SOLUTION: nxn solution
 
def n_by_n_board(board_rows): #board_rows is a list of list
    
    #find number of rows
    no_of_rows = len(board_rows)
    
    #check for columns:
    for i in range(no_of_rows):
        column_set = set()
    
        for row in board_rows:
            column_set.add(row[i])
        if len(column_set) == 1:
            return row[i]
    
    #check for rows:
    for row in board_rows:
        if len(set(row)) == 1:
            return row[0]
        
    #check for diagonals:
    diagonal_set1 = set()
    for i in range(no_of_rows):
        diagonal_set1.add(board_rows[i][i])
        if len(diagonal_set1) > 1:
            break
    if len(diagonal_set1) == 1:
        return board_rows[0][0]
    
    diagonal_set2 = set()
    for i in range(no_of_rows):
        diagonal_set2.add(board_rows[i][no_of_rows-1-i])
        if len(diagonal_set2) > 1:
            break
    if len(diagonal_set2) == 1:
        return board_rows[no_of_rows-1][0]
    

# print(n_by_n_board([["x","o","o"],["x","o","x"], ["o","o","x"]])) #o
# print(n_by_n_board([["x","x","x"],["x","o","x"], ["o","o","x"]])) #x
# print(n_by_n_board([["o","o","x"],["x","o","x"], ["o","x","o"]])) #o
# print(n_by_n_board([["x","o","o"],
#                     ["x","o","x"], 
#                     ["o",None,"x"]])) #o


# SOLUTION - Knowing the last move
def n_by_n_board_1(board_rows, row, column): #row and column numbers of the last move

    no_of_rows = len(board_rows)

    # check the row of the last move:
    last_move_row = board_rows[row]
    if len(set(last_move_row)) == 1:
        return last_move_row[0]

    # check the column of the last move:
    column_set = set()
    for i in range(no_of_rows):
        column_set.add(board_rows[i][column])
    if len(column_set) == 1:
        return board_rows[0][column]
    
    # check the diagonal of the last move:
    if row == column: # the last move is on left-to-right diagonal
        diagonal_set = {board_rows[row][column]}
        for i in range(no_of_rows):
            diagonal_set.add(board_rows[i][i])
        if len(diagonal_set) == 1:
            return board_rows[row][column]

    if row + column == no_of_rows-1: # the last move is one right-to-left diagonal
        diagonal_set = {board_rows[row][column]}
        for i in range(no_of_rows):
            diagonal_set.add(board_rows[i][no_of_rows-1-i])
        if len(diagonal_set) == 1:
            return board_rows[row][column]


print(n_by_n_board_1([["x","o","o"],
                      ["x","o","x"], 
                      ["o",None,"x"]],0,2)) #o