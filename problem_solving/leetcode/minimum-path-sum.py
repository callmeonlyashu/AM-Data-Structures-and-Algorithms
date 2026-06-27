""" Link: https://leetcode.com/problems/minimum-path-sum/"""

from typing import List
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        
        i, j = 0, 0
        def get_neighbours(i,j, g):
            """
            Get all the neighbours on left. Note, we can't go up or left so take neighbors we can include in path. Considering this
            there can be max 2 neighbors
            """
            res = []
            nbours = [(-1,0), (0,-1)]
            for k in nbours:
                row, col = i + k[0], j + k[1]
                if 0 <= row < m and 0 <= col < n:
                    res.append(g[row][col])
            return res
                
        new_grid = [[0]*n for _ in range(m)]
        new_grid[0][0] = grid[0][0]
        for i in range(m):
            for j in range(n):
                # Get all the neighbors in new grid, 
                neighbours = get_neighbours(i,j,new_grid)

                # For only one neighbors, sum that up with current grid value
                if len(neighbours) == 1:
                    new_grid[i][j] = grid[i][j] + neighbours[0]

                elif len(neighbours) == 2:
                    # For two neighbors, sum them with current grid value and take min
                    new_grid[i][j] = min(
                        grid[i][j] + neighbours[0],
                        grid[i][j] + neighbours[1]
                    )

        return new_grid[-1][-1]
