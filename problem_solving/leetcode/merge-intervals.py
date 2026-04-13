"""Link: https://leetcode.com/problems/merge-intervals/"""

from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        interv = sorted(intervals, key=lambda x: x[0])
        # print(interv)

        start, end = interv[0]

        res = []
        for i in range(1, len(interv)):
            if end >= interv[i][0]:
                end = max(interv[i][1], end)
            else:
                res.append([start, end])
                start, end = interv[i][0], max(interv[i][1], end)

        res.append([start, end])
        
        return res
