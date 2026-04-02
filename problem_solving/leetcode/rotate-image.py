"""Link: https://leetcode.com/problems/rotate-image"""

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        n = len(matrix)

        # First transpose the matrix. Switch (i, j) with (j, i)
        replaced = set()
        for i in range(n):
            for j in range(n):
                if (i, j) not in replaced:
                    replaced.add((i, j))
                    replaced.add((j, i))
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # Second Reverse each row to achieve 90 degree rotation
        for i in range(n):
            matrix[i] = matrix[i][::-1]
        
