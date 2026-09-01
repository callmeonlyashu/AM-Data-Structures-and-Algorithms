"""Link: https://leetcode.com/problems/word-search-ii/?envType=study-plan-v2&envId=top-interview-150"""

# Optimized Solution (DFS + Trie)

class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None   # None = not end of word; else holds the full word


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        # Build one shared Trie for all words (vs. searching each word separately)
        root = TrieNode()
        for word in words:
            node = root
            for ch in word:
                node = node.children.setdefault(ch, TrieNode())
            node.word = word

        m, n = len(board), len(board[0])
        res = []

        def dfs(i, j, node):
            ch = board[i][j]
            if ch not in node.children:   # no word can continue this way -> prune
                return

            nxt = node.children[ch]
            if nxt.word is not None:      # word ends here
                res.append(nxt.word)
                nxt.word = None           # avoid duplicate adds

            board[i][j] = '#'             # mark visited (like your temp swap)
            for di, dj in ((1,0), (-1,0), (0,1), (0,-1)):
                ni, nj = i+di, j+dj
                if 0 <= ni < m and 0 <= nj < n and board[ni][nj] != '#':
                    dfs(ni, nj, nxt)
            board[i][j] = ch               # always restore (no early-return skip)

            if not nxt.children:           # prune dead trie branches
                del node.children[ch]

        # one pass over the board for ALL words, instead of one pass per word
        for i in range(m):
            for j in range(n):
                dfs(i, j, root)

        return res

# TLE Solution  (DFS)

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        m, n = len(board), len(board[0])

        def dfs(i, j, k, curr_word):
            if k == len(curr_word):
                return True

            if i < 0 or i >= m or j < 0 or j >= n or board[i][j] != curr_word[k]:
                return False

            temp = board[i][j]
            board[i][j] = ''

            if dfs(i+1, j, k+1, curr_word) or \
            dfs(i-1, j, k+1, curr_word) or \
            dfs(i, j+1, k+1, curr_word) or \
            dfs(i, j-1, k+1, curr_word):

                # Set the temp back to board[i][j] for other words searching
                board[i][j] = temp
                return True

            # Set the temp back to board[i][j] for other words searching
            board[i][j] = temp
            return False

        # Separate method so that we can return immediately when the word is found
        def find_word(word):
            for i in range(m):
                for j in range(n):
                    if dfs(i, j, 0, word):
                        return True

            return False

        res = []      
        for cur_word in words:
            word_exists = find_word(cur_word)
            if word_exists:
                res.append(cur_word)

        return res


