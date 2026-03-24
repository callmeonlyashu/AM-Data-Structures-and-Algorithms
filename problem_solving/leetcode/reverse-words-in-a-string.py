"""Link: https://leetcode.com/problems/reverse-words-in-a-string/"""

class Solution:
    def reverseWords(self, s: str) -> str:
        word_array = s.split(" ")
        word_array = [w for w in word_array if w not in [" ", '']]
        # print(word_array)
        rev = word_array[::-1]
        return " ".join(rev)
        
