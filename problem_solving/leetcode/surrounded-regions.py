"""Link: https://leetcode.com/problems/surrounded-regions/"""

# Approach 1: Slow Solution
from typing import List
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        def check_o_sorrounded(i, j):
            que = deque([(i, j)])
            visited_nodes = set([(i, j)])
            break_loop = False
            while que:
                cell = que.pop()
                for nh in [(0, 0), (1,0), (-1,0), (0,-1), (0,1)]:
                    xi = cell[0] + nh[0]
                    xj = cell[1] + nh[1]
                    # handle the out of index errors
                    if (xi < 0 or xi >= m) or (xj < 0 or xj >= n) :
                        continue

                    elif board[xi][xj] == "O" and (xi in [0, m-1] or xj in [0, n-1]):
                        # Ignore if 0 is at the edges of matrix.
                        visited_nodes = set()
                        que.clear()
                        break_loop = True
                        break
                    elif board[xi][xj] == "O" and (xi, xj) not in visited_nodes:
                        que.appendleft((xi, xj))
                        visited_nodes.add((xi, xj))
                 
                if break_loop:
                    break
            
            return visited_nodes
        
        # Get all cells that needs to be replaces
        all_nodes = set()
        for x in range(m):
            for y in range(n):
                if board[x][y] == "O" and (x not in [0, m-1] or y not in [0, n-1]) and (x,y) not in all_nodes:

                    visited_nodes = check_o_sorrounded(x,y)
                    all_nodes.update(visited_nodes)

        # replace the cells
        for node in all_nodes:
            nx, ny = node
            board[nx][ny] = "X"

        

                    

        

                    
