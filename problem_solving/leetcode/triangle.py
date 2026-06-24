"""Link: https://leetcode.com/problems/triangle/description/"""

from typing import List

# Working DP Aproach
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        dp = [[] for _ in range(n)]
        dp[0] = triangle[0]

        for i in range(1,n):
            for j in range(len(triangle[i])):
                # left end
                if j == 0:
                    dp[i].append(dp[i-1][j] + triangle[i][j])
                
                # For the numbers in between
                elif 0 < j < len(triangle[i])-1:
                    dp[i].append(min(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j])
                
                # Right end
                elif j == len(triangle[i])-1:
                    dp[i].append(dp[i-1][j-1] + triangle[i][j])
        
        return min(dp[-1])

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
