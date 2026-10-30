"""Link: https://leetcode.com/problems/minimum-genetic-mutation/"""

class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: list[str]) -> int:
        queue = deque([startGene])
        visited = set()
        visited.add(startGene)
        mutations = 0

        while queue:

            length = len(queue)

            for _ in range(length):
                curr_gene = queue.popleft()
                if curr_gene == endGene:
                    return mutations

                for j in range(8):
                    for char in ["A","C","G","T"]:
                        if curr_gene[j]==char:
                            continue

                        next_gene = list(curr_gene)
                        next_gene[j]=char

                        if (("".join(next_gene)) in bank) and (("".join(next_gene))) not in visited:

                            visited.add(("".join(next_gene)))
                            queue.append(("".join(next_gene)))

            mutations+=1

        return -1




