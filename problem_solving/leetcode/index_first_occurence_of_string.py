"""
Link: https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/

"""


def strStr(haystack: str, needle: str) -> int:
    len_needle = len(needle)
    len_haystack = len(haystack)

    if len_needle == 0:
        return -1
    if len_haystack == 0:
        return -1

    # for i, ch in enumerate(haystack):
    #     for j, n in enumerate(needle):
    #         if i==j and ch==n and i != len_needle - 1:
    #             return i
    #
    # else:
    #     return -1

    for i in range(len_haystack):
        if haystack[i:i+len_needle] == needle:
            return i
    # haystack_splitted = haystack[0:3]
    # b = haystack[3:6]
    # c = haystack[6:len(haystack)+1]
    1==1


haystack = "pkksadbutsad"
needle = "sad"
index = strStr(haystack, needle)

1==1