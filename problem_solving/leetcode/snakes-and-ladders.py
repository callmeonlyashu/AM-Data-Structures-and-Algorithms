"""Link: https://leetcode.com/problems/snakes-and-ladders/"""

class Solution:
    def snakesAndLadders(self, board: list[list[int]]) -> int:
        n = len(board)
        
        i, j = n-1, 0
        cell_idx_mapping_dict = {}

        count = 1
        while i >= 0:
            if j == 0:
                while j < n:
                    cell_idx_mapping_dict[count] = (i, j)
                    j += 1
                    count += 1

            elif j == n-1:
                while j >= 0:
                    cell_idx_mapping_dict[count] = (i, j)
                    j -= 1
                    count += 1
            
            i -= 1
            if j > n-1:
                j -= 1
            
            if j < 0:
                j += 1
            
        visited = {1}
        queue = deque([(1, 0)])  # (cell, moves)
        while queue:
            cell, moves = queue.popleft()
            if cell == n * n:
                return moves
            for nxt in range(cell + 1, min(cell + 6, n * n) + 1):
                r, c = cell_idx_mapping_dict[nxt]
                dest = board[r][c] if board[r][c] != -1 else nxt
                if dest not in visited:
                    visited.add(dest)
                    queue.append((dest, moves + 1))

        return -1
