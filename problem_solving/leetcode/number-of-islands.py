"""Link: https://leetcode.com/problems/number-of-islands/"""

# Approach 1 - BFS
from typing import List
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])

        def get_all_island_neighbors(i,j):
            queue = deque([(i,j)])
            visited_notes = set((i,j))
            while queue:
                r, c = queue.pop()
                nh = [(0, 1), (0, -1), (1, 0), (-1, 0)]
                for row, col in nh:
                    curr_row, curr_col = r+row, c+col
                    if curr_row in range(0, m) and curr_col in range(0, n)\
                        and grid[curr_row][curr_col] == "1" \
                        and (curr_row, curr_col) not in visited_notes:
                        
                        queue.appendleft((curr_row,curr_col))
                        visited_notes.add((curr_row,curr_col))

            return visited_notes

        visited = set()
        island = 0
        for i in range(m):
            for j in range(n):
                cell = grid[i][j]
                if (i,j) in visited:
                    continue
                if cell == "1":
                    visited_notes = get_all_island_neighbors(i, j)
                    visited = visited | visited_notes 
                    island += 1
        
        return island


