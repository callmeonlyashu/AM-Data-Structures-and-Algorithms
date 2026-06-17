"""Link: https://leetcode.com/problems/longest-increasing-subsequence/"""

from typing import List
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1]*n
        
        for i in range(1, n):
            max_so_far = 0
            for j in range(i-1, -1, -1):
                if nums[i] > nums[j]:
                    max_so_far = max(max_so_far, dp[j])

            dp[i] = max_so_far + 1
        
        return max(dp)
