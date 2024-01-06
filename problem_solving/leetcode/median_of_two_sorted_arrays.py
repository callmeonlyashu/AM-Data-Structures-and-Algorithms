"""
Link: https://leetcode.com/problems/median-of-two-sorted-arrays/

Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).



Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
"""

class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        import math
        import copy

        # merge the array first
        l3 = copy.deepcopy(nums1)
        for e in nums2:
            l3.append(e)

        # merged_array = self.bubble_sort(copy.deepcopy(l3))
        merged_array = self.quickSort(copy.deepcopy(l3), 0, len(l3)-1)

        # Find the median
        median_index = math.floor(len(merged_array) / 2)
        if len(merged_array) % 2 != 0:
            median = merged_array[median_index]
        else:
            median = (merged_array[median_index] + merged_array[median_index - 1]) / 2
        return median

    def bubble_sort(self, arr):
        # sorting merge array using bubble sort.
        for i in range(len(arr)):
            for j in range(len(arr)):
                if arr[i] > arr[j]:
                    arr[i], arr[j] = arr[j], arr[i]

        return arr

    def partition(self, array, low, high):

        pivot = array[high]
        i = low - 1
        for j in range(low, high):
            if array[j] <= pivot:

                i = i + 1
                (array[i], array[j]) = (array[j], array[i])

        (array[i + 1], array[high]) = (array[high], array[i + 1])
        return i + 1

    # function to perform quicksort
    def quickSort(self, array, low, high):
        if low < high:
            # Find pivot element such that
            # element smaller than pivot are on the left
            # element greater than pivot are on the right
            pi = self.partition(array, low, high)

            # Recursive call on the left of pivot
            self.quickSort(array, low, pi - 1)

            # Recursive call on the right of pivot
            self.quickSort(array, pi + 1, high)

        return array



if __name__ == '__main__':
    s = Solution()
    # l1 = [7]
    # l2 = [1,4,5]
    # l1 = [3]
    # l2 = [-2, -1]
    l1 = [0,0,0,0,0]
    l2 = [-1,0,0,0,0,0,1]
    s.findMedianSortedArrays(l1, l2)