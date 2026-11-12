"""Link: https://leetcode.com/problems/find-the-difference-of-two-arrays/"""

class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        ans1 = [n for n in nums1 if n not in nums2]
        ans2 = [n for n in nums2 if n not in nums1]

        ans1 = list(set(ans1))
        ans2 = list(set(ans2))
        return [ans1, ans2]
      
