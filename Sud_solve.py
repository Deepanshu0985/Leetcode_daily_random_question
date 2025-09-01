from collections import defaultdict

def helper(board, row, col, boxes, i, j):
    if i == 9:  
        return True
    
    nexti, nextj = i, j + 1
    if nextj == 9:   
        nexti, nextj = i + 1, 0
        
    if board[i][j] != '.':
        return helper(board, row, col, boxes, nexti, nextj)
    
    for num in '123456789':
        if num not in row[i] and num not in col[j] and num not in boxes[(i//3, j//3)]:
            board[i][j] = num
            row[i].add(num)
            col[j].add(num)
            boxes[(i//3, j//3)].add(num)
            
            if helper(board, row, col, boxes, nexti, nextj):
                return True
            
            
            board[i][j] = '.'
            row[i].remove(num)
            col[j].remove(num)
            boxes[(i//3, j//3)].remove(num)
    
    return False  

def solve_sudoku(board):
    row = defaultdict(set)
    col = defaultdict(set)
    boxes = defaultdict(set)
    
    for i in range(9):
        for j in range(9):
            num = board[i][j]
            if num != '.':
                row[i].add(num)
                col[j].add(num)
                boxes[(i // 3, j // 3)].add(num)
    
    helper(board, row, col, boxes, 0, 0)


# Test
board = [
 ["5","3",".",".","7",".",".",".","."],
 ["6",".",".","1","9","5",".",".","."],
 [".","9","8",".",".",".",".","6","."],
 ["8",".",".",".","6",".",".",".","3"],
 ["4",".",".","8",".","3",".",".","1"],
 ["7",".",".",".","2",".",".",".","6"],
 [".","6",".",".",".",".","2","8","."],
 [".",".",".","4","1","9",".",".","5"],
 [".",".",".",".","8",".",".","7","9"]
]

solve_sudoku(board)
for row in board:
    print(row)
