"""Link: https://leetcode.com/problems/course-schedule/"""

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)  # adjacency list: adj[b] = [courses that need b done first]
        indegree = [0] * numCourses  # indegree[i] = how many prerequisites course i still has
        ans = []     # will hold courses in the order we "complete" them

        # Step 1: Build the graph and count indegrees
        for pair in prerequisites:
            course, preqs = pair           # pair = [course, preqs] -> take `course` after `preqs`
            adj[preqs].append(course)      # edge: preqs -> course (preqs unlocks course)
            indegree[course] += 1          # course now depends on one more prerequisite

        # Step 2: Find all "free" courses — no prerequisites needed
        queue = deque()
        for i in range(numCourses):
            if indegree[i] == 0:           # nothing blocking this course
                queue.append(i)            # it's ready to "take" right away

        # Step 3: Process courses in layers (BFS)
        while queue:
            current = queue.popleft()      # take the next ready course
            ans.append(current)            # mark it as completed

            for next_course in adj[current]:   # look at courses that needed `current`
                indegree[next_course] -= 1      # one less prerequisite blocking them
                if indegree[next_course] == 0:  # if that was their last blocker
                    queue.append(next_course)   # they're now ready too

        # Step 4: If we managed to "complete" every course, there's no cycle
        return len(ans) == numCourses


