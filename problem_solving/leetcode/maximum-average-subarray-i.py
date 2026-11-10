"""https://leetcode.com/problems/maximum-average-subarray-i/"""

class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        # The one with max sum will give max average
        curr_sum = sum(nums[0:k])
        
        max_sum = curr_sum
        for i in range(k, len(nums)):
            first_idx = nums[i-k]
            # print(f"{curr_sum} - {first_idx} + {nums[i]}")
            curr_sum = curr_sum - first_idx + nums[i]
            max_sum = max(max_sum, curr_sum)

        curr_average = max_sum/k
        return curr_average
