"""Link: https://leetcode.com/problems/max-consecutive-ones-iii/"""


# TLE Solution
class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        l, r = 0, 0
            
        # In any give window number of zeroes can't exceed k

        ones, zeroes = 0, 0
        res = 0
        while r < len(nums):
            window = nums[l:r+1]
            count = len([n for n in window if n == 0])
            if count <= k:
                res = max(len(window), res)
            if nums[r] == 0:
                if zeroes < k:
                    zeroes += 1
                    r += 1
                else:
                    l += 1
                    if nums[l-1] == 0:
                        zeroes -= 1
            else:
                if zeroes <= k:
                    ones += 1
                    r += 1
                
        return res
                
                
            
            

                    
                
