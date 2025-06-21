def in_row(num, row, board):
    return num in board[row]

def in_col(num, col, board):
    return num in board[col]

def in_box(num, row, col, board):
    box_row = (row//3)*3
    box_col = (col//3)*3
    for i in range(box_row, box_row+3):
        for j in range(box_col, box_col+3):
            if board[i][j] == num:
                return True
    return False

def is_valid(num, row, col, board):
    return not (in_row(num,row,board) or in_col(num,col,board) or in_box(num, row, col, board))

def find_empty_position(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j
            
    return None

def find_solution(board):
    empty_pos = find_empty_position(board)

    if not empty_pos:
        return True
    row, col = empty_pos
    for num in range(1,10):
        if is_valid(num,row,col,board):
            board[row][col]=num
            if find_solution(board):
                return True
            board[row][col] = 0

    return False

def solution(board):
    find_solution(board)
    return board