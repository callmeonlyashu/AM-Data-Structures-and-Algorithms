"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Link: https://leetcode.com/problems/two-sum/

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
"""


class Solution:
    def twoSum(self, nums, target):
        for index in range(len(nums)):
            first_num = nums[index]
            second_num = target - first_num
            is_available, index2 = self.search(second_num, nums, index)
            if is_available:
                return [index, index2]

    def search(self, second_num, nums, indexes_to_skip):
        for index in range(len(nums)):
            if index > indexes_to_skip:
                if second_num == nums[index]:
                    return True, index

        return False, 0





if __name__ == '__main__':
    solution = Solution()
    solution.twoSum([3,2,4], target=6)