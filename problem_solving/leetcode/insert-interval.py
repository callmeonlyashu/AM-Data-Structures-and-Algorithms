"""Link: https://leetcode.com/problems/insert-interval/"""

# Approach 1
from typing import List
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        # Append the interval 
        intervals.append(newInterval)

        # Sort the interval
        intervals = sorted(intervals, key=lambda x: x[0])

        # print(intervals)

        start, end = intervals[0]
        res = []
        for i in range(1, len(intervals)):
            if end >= intervals[i][0]:
                end = max(end, intervals[i][1])
            else:
                res.append([start, end])
                start, end = intervals[i]

        res.append([start, end])

        return res
