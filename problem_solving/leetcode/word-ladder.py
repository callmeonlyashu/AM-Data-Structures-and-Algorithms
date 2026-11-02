"""Link: https://leetcode.com/problems/word-ladder/"""

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        queue = deque([beginWord])
        visited = set()
        visited.add(beginWord)
        transformations = 1

        wordList = set(wordList)

        while queue:

            length = len(queue)

            for _ in range(length):
                curr_word = queue.popleft()

                if curr_word == endWord:
                    return transformations

                for j in range(len(beginWord)):
                    for char in string.ascii_lowercase:
                        if curr_word[j]==char:
                            continue

                        next_word = list(curr_word)
                        next_word[j]=char

                        if (("".join(next_word)) in wordList) and (("".join(next_word))) not in visited:

                            visited.add(("".join(next_word)))
                            queue.append(("".join(next_word)))

            transformations+=1

        return 0

        
