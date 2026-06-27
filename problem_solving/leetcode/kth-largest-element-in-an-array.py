"""Link: https://leetcode.com/problems/kth-largest-element-in-an-array/"""

from typing import List
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Convert to negatives as Python support Min Heap only.
        nums = [i*-1 for i in nums]
        heapq.heapify(nums) 

        for i in range(k):
            # Remove top K elements to get kth largest
            smallest = heapq.heappop(nums)

        return smallest*-1
