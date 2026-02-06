"""Link: https://leetcode.com/problems/jump-game/?envType=study-plan-v2&envId=top-interview-150"""

from typing import List
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        q = deque()
        q.append((0, nums[0]))
        visited = set()
        visited.add(0)
        if len(nums) == 1:
            return True
        
        while q:
            index, curr_step = q.popleft()
            for i in range(curr_step):
                next_index = index+i+1
                if next_index >= len(nums)-1:
                    return True
                
                if next_index not in visited:
                    q.append((next_index, nums[next_index]))
                    visited.add(next_index)
        
        return False


