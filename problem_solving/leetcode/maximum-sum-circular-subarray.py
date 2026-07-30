"""Link: https://leetcode.com/problems/maximum-sum-circular-subarray/"""

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
