"""
Link: https://leetcode.com/problems/4sum/description/

Description:
Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.



Example 1:
    Input: nums = [1,0,-1,0,-2,2], target = 0
    Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

Example 2:
    Input: nums = [2,2,2,2,2], target = 8
    Output: [[2,2,2,2]]
"""


class Solution():

    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:

        nums.sort()
        result = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                left = j+1
                right = len(nums)-1
                cur_sum = nums[i] + nums[j] + nums[left] + nums[right]
                if cur_sum == target:
                    result.append([nums[i], nums[j], nums[left], nums[right]])
                while left < right and left == left + 1:
                    left += 1
                while left < right == right - 1:
                    right -= 1

                if cur_sum < target:
                    left += 1
                else:
                    right -= 1

        return result




if __name__ == "__main__":
    sol = Solution()
    a = sol.fourSum([1,0,-1,0,-2,2], 0)
    # b = sol.fourSum([2,2,2,2,2], 8)

    1==1
