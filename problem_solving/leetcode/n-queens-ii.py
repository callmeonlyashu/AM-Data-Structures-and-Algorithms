"""Link: https://leetcode.com/problems/n-queens-ii/?envType=study-plan-v2&envId=top-interview-150"""

class Solution:
    def totalNQueens(self, n: int) -> int:
        board = [["."]*n for _ in range(n)]

        col = set()
        posDiag = set()
        negDiag = set()

        res = []
        def dfs(r):
            if r == n:
                cp_board = ["".join(row) for row in board]
                res.append(cp_board)
                return res

            for c in range(n):
                if c in col or (r+c) in posDiag or (r-c) in negDiag:
                    continue

                col.add(c)
                posDiag.add(r+c)
                negDiag.add(r-c)
                board[r][c] = "Q"

                dfs(r+1)
                
                col.remove(c)
                posDiag.remove(r+c)
                negDiag.remove(r-c)
                board[r][c] = "."

        dfs(0)
        return len(res)
            
