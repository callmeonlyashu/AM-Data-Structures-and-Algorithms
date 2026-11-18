"""Link: https://leetcode.com/problems/max-number-of-k-sum-pairs/"""

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        l, r = 0, len(nums)-1

        nums.sort()

        pairs = 0
        while l < r:
            if nums[l] + nums[r] == k:
                pairs += 1
                l += 1
                r -= 1
            if nums[l] + nums[r] > k:
                r -= 1
            if nums[l] + nums[r] < k:
                l += 1

        return pairs
            
