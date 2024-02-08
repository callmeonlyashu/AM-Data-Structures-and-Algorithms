"""
Link: https://leetcode.com/problems/container-with-most-water/description/

You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.


Example 1:


Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
Example 2:

Input: height = [1,1]
Output: 1

"""


class Solution:
    # def maxArea(self, height: list[int]) -> int:
    #     maximum = 0
    #     for i in range(len(height)):
    #         inner = []
    #         for j in range(len(height)):
    #             if height[i] > height[j]:
    #                 length = height[j]
    #             else:
    #                 length = height[i]
    #             breadth = abs(j - i)
    #
    #             area = length * breadth
    #             if area >= maximum:
    #                 maximum = area
    #
    #     return maximum

    def maxArea(self, height: list[int]) -> int:

        i = 0
        j = len(height)-1
        max_area = 0
        while i <= j:
            if height[i] < height[j]:
                breadth = abs(i-j)
                length = height[i]
                area = breadth*length
                if area > max_area:
                    max_area = area
                i += 1
            else:
                breadth = abs(i-j)
                length = height[j]
                area = breadth*length
                if area > max_area:
                    max_area = area
                j -= 1

        return max_area


if __name__ == '__main__':
    sol = Solution()
    sol.maxArea([1,8,6,2,5,4,8,3,7])
    # sol.maxArea([1,1])
