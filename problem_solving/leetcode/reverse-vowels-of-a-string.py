"""Link: https://leetcode.com/problems/reverse-vowels-of-a-string/"""

class Solution:
    def reverseVowels(self, s: str) -> str:
        left, right = 0, len(s)-1

        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U', }
        s = list(s)
        while left < right:
            
            if s[left] in vowels:
                while s[right] not in vowels:
                    right -= 1
                                
                s[left], s[right] = s[right],  s[left]
                
                right -= 1
            left += 1
        
        return "".join(s)

            
