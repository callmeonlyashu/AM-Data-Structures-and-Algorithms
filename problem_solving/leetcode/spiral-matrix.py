"""Link: https://leetcode.com/problems/spiral-matrix/"""

from typing import List
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        circle = 0
        visited = set()

        res = []

        while len(visited) != m*n:
        
            i, j = circle, circle
            max_m, max_n = m-circle, n-circle

            # Move Right
            while j < max_n:
                if (i, j) not in visited:
                    res.append(matrix[i][j])
                    visited.add((i, j))
                j += 1

            # Reduce j back to j-1
            j -= 1
            i += 1

            # Move Down
            while i < max_m:
                if (i, j) not in visited:
                    res.append(matrix[i][j])
                    visited.add((i, j))
                i += 1
            
            # Reduce i back to i-1
            i -= 1
            j -= 1

            # Move Left
            while j >= circle:
                if (i, j) not in visited:
                    res.append(matrix[i][j])
                    visited.add((i, j))
                j -= 1

            # Reduce j back to j-1
            i -= 1
            j += 1

            # Move Up
            while i > circle:
                if (i, j) not in visited:
                    res.append(matrix[i][j])
                    visited.add((i, j))
                i -= 1

            # print(res)
            circle += 1
        
        return res
