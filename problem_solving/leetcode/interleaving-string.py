"""Link: https://leetcode.com/problems/interleaving-string/"""

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        # Memoization Approach
        if len(s1) + len(s2) != len(s3):
            return False
            
        @cache
        def dfs(i, j):
            if i == len(s1) and j == len(s2):
                return True
            choose_s1, choose_s2 = False, False
            if i < len(s1) and s1[i] == s3[i + j]:
                choose_s1 = dfs(i + 1, j)
            if j < len(s2) and s2[j] == s3[i + j]:
                choose_s2 = dfs(i, j + 1)

            return choose_s1 or choose_s2

        return dfs(0, 0)

        # Tabulation DP Approach
        m, n = len(s1), len(s2)
        if m + n != len(s3):
            return False

        # dp[i][j] = True if s3[:i+j] can be formed by interleaving s1[:i] and s2[:j]
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True

        for i in range(m + 1):
            for j in range(n + 1):
                if i == 0 and j == 0:
                    continue
                take_s1 = i > 0 and dp[i-1][j] and s1[i-1] == s3[i+j-1]
                take_s2 = j > 0 and dp[i][j-1] and s2[j-1] == s3[i+j-1]
                dp[i][j] = take_s1 or take_s2

        return dp[m][n]
