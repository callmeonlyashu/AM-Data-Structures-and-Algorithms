"""
Link: https://leetcode.com/problems/3sum/

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Example 1:

    Input: nums = [-1,0,1,2,-1,-4]
    Output: [[-1,-1,2],[-1,0,1]]
    Explanation:
    nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
    nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
    nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
    The distinct triplets are [-1,0,1] and [-1,-1,2].
    Notice that the order of the output and the order of the triplets does not matter.

Example 2:

    Input: nums = [0,1,1]
    Output: []
    Explanation: The only possible triplet does not sum up to 0.

Example 3:

    Input: nums = [0,0,0]
    Output: [[0,0,0]]
    Explanation: The only possible triplet sums up to 0.
"""


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        import copy
        result = []

        if len(nums) < 3:
            return []

        if len(nums) == 3 and sum(nums) == 0:
            return [nums]

        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j:
                    break
                target = 0 - (nums[i]+nums[j])
                my_nums = copy.deepcopy(nums)
                del my_nums[i]
                del my_nums[j]
                if target in my_nums:
                    my_array = [nums[i], nums[j], target]
                    my_array.sort()
                    if my_array not in result:
                        result.append(my_array)

                del my_nums

        return result



if __name__ == '__main__':
    sol = Solution()
    # sol.threeSum([-1,0,1,2,-1,-4])
    a = sol.threeSum([-10,-7,-3,-9,-8,-9,-5,6,0,6,4,-15,-12,3,-12,-10,-5,-5,2,-4,13,8,-9,6,-11,11,3,-13,-3,14,-9,2,14,-5,8,-9,-7,-12,5,1,2,-6,1,5,4,-4,3,7,-2,12,10,-3,6,-14,-12,10,12,7,12,-14,-2,11,4,-10,13,-11,-4,-8,-15,-14,8,-6,-12,-14,6,7,-3,-14,-1,11,14,-6,-15,5,-13,-12,0,14,2,-11,-14,8,-15,-3,13,14,-7,-14,13,-15,10,-2,-14,13])
    1==1

