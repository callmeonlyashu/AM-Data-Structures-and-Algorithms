"""

URL: https://leetcode.com/problems/reverse-integer/description/

Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21
"""

class Solution:
    def reverse(self, x: int) -> int:
        arr = []

        is_negative = False
        if x < 0:
            x = abs(x)
            is_negative = True

        num = x
        while True:
            if num <= 0:
                break
            rem = num % 10
            num = num // 10
            arr.append(rem)

        k = 0
        length = len(arr) - 1
        for n in range(len(arr)):
            k = arr[n]*(10**length)+k
            length -= 1

        if k < -2**31 or k > 2**31:
            return 0

        if is_negative:
            return k * -1

        return k