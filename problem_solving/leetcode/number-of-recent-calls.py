"""Link: https://leetcode.com/problems/number-of-recent-calls/"""

class RecentCounter:

    def __init__(self):
        self.queue = deque([])
        self.num_requests = 0

    def ping(self, t: int) -> int:
        self.queue.append(t)
        while self.queue[0] < t - 3000:
            self.queue.popleft()  # drop old

        return len(self.queue)
