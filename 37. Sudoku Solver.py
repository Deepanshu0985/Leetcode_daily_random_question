import sys
sys.setrecursionlimit(10**6)   # not really needed, but safe

from typing import List
board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]

class Solution:
    def issafe(self, board, row, col, digit):
        digit = str(digit)
        for i in range(9):
            if board[i][col] == digit or board[row][i] == digit:
                return False
        startrow, startcol = 3 * (row // 3), 3 * (col // 3)
        for i in range(startrow, startrow + 3):
            for j in range(startcol, startcol + 3):
                if board[i][j] == digit:
                    return False
        return True

    def helper(self, board, row, col):
        if row == 9:
            return True
        nxtrow, nxtcol = row, col + 1
        if nxtcol == 9:
            nxtrow, nxtcol = row + 1, 0
        if board[row][col] != ".":
            return self.helper(board, nxtrow, nxtcol)
        for digit in range(1, 10):
            if self.issafe(board, row, col, digit):
                board[row][col] = str(digit)
                if self.helper(board, nxtrow, nxtcol):
                    return True
                board[row][col] = "."
        return False

    def solveSudoku(self, board: List[List[str]]) -> None:
        self.helper(board, 0, 0)
        
        

class Solutionoptimizes:
    def __init__(self):
        self.rows = [set() for _ in range(9)]
        self.cols = [set() for _ in range(9)]
        self.boxes = [set() for _ in range(9)]

    def issafe(self, row, col, digit):
        box_id = (row // 3) * 3 + (col // 3)
        return not (digit in self.rows[row] or digit in self.cols[col] or digit in self.boxes[box_id])

    def find_best_cell(self, board):
        """Return (row, col, candidates) with fewest options"""
        best = None
        min_options = 10
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    candidates = []
                    for d in map(str, range(1, 10)):
                        if self.issafe(i, j, d):
                            candidates.append(d)
                    if len(candidates) < min_options:
                        min_options = len(candidates)
                        best = (i, j, candidates)
                        if min_options == 1:  # perfect cell
                            return best
        return best

    def backtrack(self, board):
        cell = self.find_best_cell(board)
        if not cell:
            return True  # solved

        row, col, candidates = cell
        for d in candidates:
            # place digit
            board[row][col] = d
            self.rows[row].add(d)
            self.cols[col].add(d)
            self.boxes[(row // 3) * 3 + (col // 3)].add(d)

            if self.backtrack(board):
                return True

            # backtrack
            board[row][col] = "."
            self.rows[row].remove(d)
            self.cols[col].remove(d)
            self.boxes[(row // 3) * 3 + (col // 3)].remove(d)

        return False

    def solveSudoku(self, board: List[List[str]]) -> None:
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    d = board[i][j]
                    self.rows[i].add(d)
                    self.cols[j].add(d)
                    self.boxes[(i // 3) * 3 + (j // 3)].add(d)

        self.backtrack(board)

#example usage
obj = Solutionoptimizes()
obj.solveSudoku(board)

for i in board:
    print(i)