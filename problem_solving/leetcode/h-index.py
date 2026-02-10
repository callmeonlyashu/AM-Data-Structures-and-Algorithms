"""Link: https://leetcode.com/problems/h-index/?envType=study-plan-v2&envId=top-interview-150"""

from typing import List

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()

        max_citations = 0
        for i in range(len(citations)):
            curr = 0
            for j in range(i, i+citations[i]):
                if j >= len(citations):
                    break
                if citations[j] >= citations[i]:
                    curr += 1

            max_citations = max(max_citations, curr)
        
        return max_citations
