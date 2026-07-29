"""Link: https://leetcode.com/problems/word-search/"""

# Backtracking 

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def backtrack(i, j, k):
            if k == len(word):
                return True
            
            # Handle out of indexes and if char in word at k doesn't match current grid value
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != word[k]:
                return False
            
            # Save current cell to temp, this is to mark board[i][j] as 
            # visited so that we don't use same cell twice
            temp = board[i][j]
            board[i][j] = ''
            
            # Check if any of the neighbour matches the next index k+1
            if backtrack(i+1, j, k+1) or \
                backtrack(i-1, j, k+1) or \
                backtrack(i, j+1, k+1) or \
                backtrack(i, j-1, k+1):
                return True
            
            # Before returning assign back temp value for next set of recurrsion
            board[i][j] = temp
            return False
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if backtrack(i, j, 0):
                    return True
        return False
