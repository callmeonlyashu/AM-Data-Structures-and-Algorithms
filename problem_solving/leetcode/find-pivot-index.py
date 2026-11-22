"""Link: https://leetcode.com/problems/find-pivot-index/"""

class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        left, right = 0, sum(nums[1:])
        for i in range(len(nums)):
            if left == right:
                return i

            left += nums[i]
            if (i+1) < len(nums):
                right -= nums[i+1]

        right -= nums[i]
        if left == right:
            return i

        return -1
