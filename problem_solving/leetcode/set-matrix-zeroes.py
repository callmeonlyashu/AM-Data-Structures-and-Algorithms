"""Link: https://leetcode.com/problems/set-matrix-zeroes/"""

from typing import List
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        total_r, total_c = len(matrix), len(matrix[0])
        zero_rows = set()
        zero_cols = set()

        # Get all the rows and columns with zeroes
        for r in range(total_r):
            for c in range(total_c):
                if matrix[r][c] == 0:
                    zero_rows.add(r)
                    zero_cols.add(c)

        # Loop through the rows and make the columns zero
        for i in range(total_r):
            for j in zero_cols:
                matrix[i][j] = 0

        # Loop through the columns and make the rows zero
        for i in zero_rows:
            for j in range(total_c):
                matrix[i][j] = 0


