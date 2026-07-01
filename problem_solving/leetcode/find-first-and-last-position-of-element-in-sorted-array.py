"""https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/"""

from typing import List
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)

        def binary_search(is_left):
            idx = -1
            l, r = 0, n-1
            while l <= r:
                mid = (r+l)//2
                if nums[mid] == target:
                    if is_left:
                        idx = mid
                        r = mid-1
                    else:
                        idx = mid
                        l = mid + 1
                
                if nums[mid] < target:
                    l = mid + 1
                
                if nums[mid] > target:
                    r = mid - 1
            return idx

        # To get the left most index
        l_idx = binary_search(is_left=True)
        # To get the right most index
        r_idx = binary_search(is_left=False)
        
        return [l_idx, r_idx]

        


                

