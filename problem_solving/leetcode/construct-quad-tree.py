"""Link: https://leetcode.com/problems/construct-quad-tree/"""

from typing import List
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
         
        def dfs(n, r, c):
            
            # Check if all the values are same in grid
            all_same = True
            for i in range(n):
                for j in range(n):
                    if grid[r][c] != grid[r+i][c+j]:
                        all_same = False
                        break

            # If all same, make it leaf node
            if all_same:
                return Node(val=grid[r][c], isLeaf=True)

            # Keep splitting the grid into half
            n = n//2

            # Ge the child
            topleft = dfs(n, r, c)
            topright = dfs(n, r, c+n)
            bottomleft = dfs(n, r+n, c)
            bottomright = dfs(n, r+n, c+n)

            return Node(val=0,
                        isLeaf=False, 
                        topLeft = topleft,
                        topRight = topright,
                        bottomLeft = bottomleft,
                        bottomRight = bottomright)

        length = len(grid)
        tree = dfs(length, 0, 0)
        return tree


