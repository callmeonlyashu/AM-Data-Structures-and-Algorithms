class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        result = []
        nums.sort()

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue  # Skip duplicate elements

            left, right = i + 1, len(nums) - 1

            while left < right:
                curr_sum = nums[i] + nums[left] + nums[right]

                if curr_sum == 0:
                    result.append([nums[i], nums[left], nums[right]])

                    # Skip duplicate elements
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1
                elif curr_sum < 0:
                    left += 1
                else:
                    right -= 1

        return result


if __name__ == '__main__':
    sol = Solution()
    value = sol.threeSum([-1,0,1,2,-1,-4])
    # value2 = sol.threeSum([-10,-7,-3,-9,-8,-9,-5,6,0,6,4,-15,-12,3,-12,-10,-5,-5,2,-4,13,8,-9,6,-11,11,3,-13,-3,14,-9,2,14,-5,8,-9,-7,-12,5,1,2,-6,1,5,4,-4,3,7,-2,12,10,-3,6,-14,-12,10,12,7,12,-14,-2,11,4,-10,13,-11,-4,-8,-15,-14,8,-6,-12,-14,6,7,-3,-14,-1,11,14,-6,-15,5,-13,-12,0,14,2,-11,-14,8,-15,-3,13,14,-7,-14,13,-15,10,-2,-14,13])
    1==1

