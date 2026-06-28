""" https://leetcode.com/problems/filter-occupied-intervals/ """

from typing import List
class Solution:
    def filterOccupiedIntervals(self, occupiedIntervals: List[List[int]], freeStart: int, freeEnd: int) -> List[List[int]]:

        occupiedIntervals = sorted(occupiedIntervals, key=lambda x: x[0])

        start, end = occupiedIntervals[0]

        # First merge all the intervals
        merged = []
        cur_s, cur_e = 0, 0
        for i in range(1, len(occupiedIntervals)):
            cur_s, cur_e = occupiedIntervals[i]

            # +1 is to check if interval touches
            if end+1 >= cur_s:
                end = max(end, cur_e)
            else:
                merged.append([start, end])
                start, end = occupiedIntervals[i]

        merged.append([start, end])

        # Once merged, filter out the integers based on freeStart and freeEnd 
            
        res = []
        for s, e in merged:
            # 1. Check for the part before the free interval
            left_end = min(e, freeStart - 1)
            if s <= left_end:
                res.append([s, left_end])
            
            # 2. Check for the part after the free interval
            right_start = max(s, freeEnd + 1)
            if right_start <= e:
                res.append([right_start, e])
            
        return res
