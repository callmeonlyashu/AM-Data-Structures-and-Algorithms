"""Link: https://leetcode.com/problems/summary-ranges/"""

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        i = 0
        if not len(nums):
            return []

        start_interval = nums[i]
        res = []
        for i in range(1, len(nums)):
            if nums[i-1]+1 != nums[i]:
                if start_interval != nums[i-1]:
                    res.append(f"{start_interval}->{nums[i-1]}")
                else:
                    res.append(f"{start_interval}")
                start_interval = nums[i]

        if start_interval != nums[i]:
            res.append(f"{start_interval}->{nums[i]}")
        else:
            res.append(f"{start_interval}")
        return res
        
