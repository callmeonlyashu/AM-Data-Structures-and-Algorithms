"""Link: https://leetcode.com/problems/powx-n/"""
class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        # Handle negative exponent
        if n < 0:
            x = 1 / x
            n = -n
        
        res = 1
        current_product = x
        
        while n > 0:
            # If the current bit is 1, multiply by the current base
            if n % 2 == 1:
                res *= current_product
            
            # Square the base and halve the exponent
            current_product *= current_product
            n //= 2
            
        return res
    
if __name__ == "__main__":
    solution = Solution()
    print(solution.myPow(2.0, 10))  # Output: 1024.0
    print(solution.myPow(2.0, -2))  # Output: 0.25
    print(solution.myPow(2.1, 3))   # Output: 9.261