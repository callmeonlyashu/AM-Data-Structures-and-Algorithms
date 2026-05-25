"""Link: https://leetcode.com/problems/trapping-rain-water/"""

# Approach 1: TLE
from typing import List
class Solution:
    def trap(self, height: List[int]) -> int:
        max_left = 0
        n = len(height)

        total_water = 0
        for i in range(1, n):
            curr_bar = height[i]
            max_left = max(height[i-1], max_left)
            max_right = 0
            for j in range(i+1, n):
                max_right = max(max_right, height[j])
                if max_right > max_left:
                    break

            curr_water = min(max_left, max_right) - curr_bar
            if curr_water > 0:
                total_water += curr_water

        return total_water
        

