"""Link: https://leetcode.com/problems/valid-sudoku/description/"""
from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        total_rows = len(board)
        total_cols = len(board[0])

        def check_column(i, j):
            nums = []
            while i < total_rows:
                if board[i][j].isdigit():
                    nums.append(board[i][j])
                i += 1

            # print("cols", nums)
            return len(set(nums)) == len(nums)

        def check_row(i, j):
            nums = []
            while j < total_cols:
                if board[i][j].isdigit():
                    nums.append(board[i][j])
                j += 1

            # print("rows", nums)
            return len(set(nums)) == len(nums)

        def check_grid(i, j):
            grid_row = j//3
            grid_col = i//3
            # print("grid_row", grid_row)
            # print("grid_col", grid_col)

            row_idx = [i for i in range(grid_row*3, (grid_row*3)+3)]
            col_idx = [i for i in range(grid_col*3, (grid_col*3)+3)]

            nums = []
            for r in row_idx:
                for c in col_idx:
                    if board[r][c].isdigit():
                        nums.append(board[r][c])
            
            # print("grid", nums)
            return len(set(nums)) == len(nums)
            

        for m in range(total_rows):
            for n in range(total_cols):
                if not check_column(m,n) or not check_row(m,n) or not check_grid(m,n):
                    return False

        return True
