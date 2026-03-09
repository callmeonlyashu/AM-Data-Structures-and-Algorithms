"""Link: https://leetcode.com/problems/substring-with-concatenation-of-all-words/"""

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        word_size = len(words[0])
        total_words = len(words)
        
        def get_words_count(w):
            wc = defaultdict(int)
            for i in w:
                wc[i] += 1
            return wc

        def get_words_count_from_string(sent):
            i = 0
            st = ""
            cnt = []
            for char in sent:
                st += char
                i += 1
                if i == word_size:
                    cnt.append(st)
                    st = ""
                    i = 0
            
            return cnt

        words_count = get_words_count(words)
        l = 0
        r = word_size*total_words

        res = []
        while r <= len(s):
            curr_wind = s[l:r]
            # print(curr_wind)
            curr_wind_arr = get_words_count_from_string(curr_wind)
            # print(curr_wind_arr)

            curr_count = get_words_count(curr_wind_arr)
            # print("curr_count", dict(curr_count))
            # print("words_count", dict(words_count))
            # print("---------------------------")
            if curr_count == words_count:
                res.append(l)

            l += 1
            r += 1

        return res


            
            
