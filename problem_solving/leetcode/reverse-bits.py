"""Link: https://leetcode.com/problems/reverse-bits/"""

class Solution:
    def reverseBits(self, n: int) -> int:
        bin_n = bin(n)[2:].zfill(32)
        res = int(bin_n[::-1], 2)
        return res
