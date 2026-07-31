"""Link: https://leetcode.com/problems/maximum-sum-circular-subarray/"""

# Kadane's Algorithm
class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        curr_max = nums[0]
        max_sum = nums[0]

        curr_min = nums[0]
        min_sum = nums[0]

        n = len(nums)
        total = nums[0]

        for i in range(1, n):
            total += nums[i]
            # Get curr max and max_sum so far
            curr_max = max(curr_max + nums[i], nums[i])
            max_sum = max(max_sum, curr_max)

            # Get curr min and min_sum so far
            curr_min = min(curr_min + nums[i], nums[i])
            min_sum = min(min_sum, curr_min)
        
        # max_sum is 0 means no positive numbers are there in list
        if max_sum < 0:
            return max_sum

        # For circular sub_array sum(nums)-min_sum is needed to check if sub_array is round the corner        
        return max(max_sum, total-min_sum)


# Other Approach 
from typing import List
class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)
        P = [0] * (2 * n + 1)
        for i in range(2 * n):
            P[i + 1] = P[i] + nums[i % n]
        
        ans = nums[0]
        dq = deque([0])  # indices into P, increasing P values front to back

        for j in range(1, 2 * n + 1):
            # window constraint: subarray length <= n
            while dq and dq[0] < j - n:
                dq.popleft()

            ans = max(ans, P[j] - P[dq[0]])

            while dq and P[dq[-1]] >= P[j]:
                dq.pop()
            dq.append(j)

        return ans
