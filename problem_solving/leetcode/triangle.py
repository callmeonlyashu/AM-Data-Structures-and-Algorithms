"""Link: https://leetcode.com/problems/triangle/description/"""

from typing import List

# Failed DP Approach

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = [None]*len(triangle)
        dp[0] = (0, triangle[0][0])

        for i in range(1, len(triangle)):
            idx, num = dp[i-1]
            if (num+triangle[i][idx]) < (num+triangle[i][idx+1]):
                dp[i] = (idx, num+triangle[i][idx])
            else:
                dp[i] = (idx+1, num+triangle[i][idx+1])
                    
        return dp[-1][-1]
