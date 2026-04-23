"""Link: https://leetcode.com/problems/factorial-trailing-zeroes"""

class Solution:
    def trailingZeroes(self, n: int) -> int:
        sys.set_int_max_str_digits(100000)
        if n in [0,1,2,3,4]:
            return 0

        dp = [0]*2
        dp[0] = 1
        dp[1] = 2

        i = 3
        while i <= n:
            dp[1] = dp[1] * i
            i += 1
        
        fac = str(dp[-1])

        i = len(fac)-1
        count = 0
        while i >= 0:
            if fac[i] != "0":
                return count
            else:
                count += 1
            
            i -= 1

        return count


# Solution 2: 
# Count number of factors of 5 in number

class Solution:
    def trailingZeroes(self, n: int) -> int:
        if n < 5:
            return 0

        res = 0
        while n >= 5:
            res += int(n/5)
            n = int(n/5)

        return res

