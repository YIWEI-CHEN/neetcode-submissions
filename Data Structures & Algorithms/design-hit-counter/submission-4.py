"""
# hit <= past 300 sec
hit(1) time=1, count = 1
hit(1) time=1, count += 1
bucket = [timestamp, counts]
hit(1): [time=1, count =2], total = 2
hit(2), [time=2, count=1], total = 3
hit(300), [time=300, count=1], total =4
`getHit(300)`: valid = 300 - 300 = 0, any timestamp > 0, total = 2 + 1 + 1 = 4
valid timestamp > timestamp - 300
var total = 4
for invalid timestamp <= 300 - 300 = 0, remove those hits from total

queue, put oldest at start, new at end, check last element
check oldest, queue top left
"""
from collections import deque

class HitCounter:

    def __init__(self):
        self.hits = deque()  # bucket = [timestamp, counts], not tuple, no way to adjust tuple value on fly
        self.total = 0

    def hit(self, timestamp: int) -> None:
        # Time: O(1), only check last element in queue
        # Space: O(self.hits), O(300)
        if self.hits and self.hits[-1][0] == timestamp:
            self.hits[-1][1] += 1
        else:
            self.hits.append([timestamp, 1])
        self.total += 1

    def getHits(self, timestamp: int) -> int:
        # check counts in the valid time range
        # remove those invalid hits, invalid <= timestamp - 300
        # Time: O(k), k is number of timestamp in the queue
        # Space: O(300)
        while self.hits and self.hits[0][0] <= timestamp - 300:
            _, counts = self.hits.popleft()
            self.total -= counts
        return self.total
        


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
