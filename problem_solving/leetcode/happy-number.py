"""Link: https://leetcode.com/problems/happy-number/"""


class Solution:
    def isHappy(self, n: int) -> bool:
        
        nums_so_far = []

        while n not in nums_so_far:
            nums_so_far.append(n)
            lst = [int(i) for i in list(str(n))]
            n = sum([i**2 for i in lst])

            if n == 1:
                return True

        return False
