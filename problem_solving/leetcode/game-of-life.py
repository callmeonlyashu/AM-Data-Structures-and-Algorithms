"""Link: https://leetcode.com/problems/game-of-life/"""

from typing import List
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        m, n = len(board), len(board[0])
        def get_live_neighbors(i, j):
            live = 0
            for row in [i, i-1, i+1]:
                for col in [j, j-1, j+1]:
                    if row == i and col == j:
                        continue
                    else:
                        if row in range(0, m) and col in range(0, n):
                            if board[row][col] == 1:
                                live += board[row][col]
            return live

        res = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                curr_live_neighbors = get_live_neighbors(i, j)
                curr_cell = board[i][j]
                if curr_cell == 1:
                    if curr_live_neighbors < 2 or curr_live_neighbors > 3:
                        res[i][j] = 0
                    else:
                        res[i][j] = board[i][j]
                else:
                    if curr_live_neighbors == 3:
                        res[i][j] = 1
                    else:
                        res[i][j] = board[i][j]

        board[:] = copy.deepcopy(res)
