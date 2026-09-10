
"""Link: https://leetcode.com/problems/edit-distance/"""
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """
            https://en.wikipedia.org/wiki/Levenshtein_distance

            declare int d[0..m, 0..n]

            for i from 0 to m:
                d[i, 0] := i

            for j from 0 to n:
                d[0, j] := j

            for i from 1 to m:
                for j from 1 to n:
                    if s[i] = t[j]:
                        substitutionCost := 0
                    else:
                        substitutionCost := 1

                    d[i, j] := minimum(
                        d[i-1, j]   + 1,                  // deletion of s[i]
                        d[i, j-1]   + 1,                  // insertion of t[j]
                        d[i-1, j-1] + substitutionCost    // match or substitution
                    )

            return d[m, n]
        """
        m = len(word1)
        n = len(word2)

        dp = [[0]*(n+1) for _ in range(m+1)]
        substitutionCost = 0

        for i in range(m+1):
            dp[i][0] = i

        for j in range(n+1):
            dp[0][j] = j

        for i in range(1, m+1):
            for j in range(1, n+1):
                if word1[i-1] == word2[j-1]:
                    substitutionCost = 0
                else:
                    substitutionCost = 1

                dp[i][j] = min(
                    dp[i-1][j]   + 1,                  # deletion of s[i]
                    dp[i][j-1]   + 1,                  # insertion of t[j]
                    dp[i-1][j-1] + substitutionCost    # match or substitution
                )

        return dp[m][n]
