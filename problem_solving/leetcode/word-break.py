"""Link: https://leetcode.com/problems/word-break/"""

from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [None]*(len(s)+1)
        dp[0] = True

        for i in range(len(s)+1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break
                else:
                    dp[i] = False
        
        return dp[-1]
