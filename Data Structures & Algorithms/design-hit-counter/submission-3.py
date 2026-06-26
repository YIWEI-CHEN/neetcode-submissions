"""
1. #hits past 300 sec -> sliding win
2. bucket group hits with same timestamp, bucket = [timestamp, counts]
3. `hit`, last timestamp in bucket, if match timestamp, count+=1, otherwise, append new time with count
4. `getHits`, valid hits with timestamp > t - 300, remove those hits < t - 300. total var
    hit(1): [t=1, count=1], total = 1
    hit(2): [t=2, count=1], total = 2
    hit(3): [t=3, count=1], total = 3
    getHits(4): valid timestamp = 4 - 300 = -296, t=1, 2,3 > -296 return total = 3
    hit(300): [t=300, count=1], total = 4
    getHits(300), valid = 300 - 300 = 0; t=1,2,3,300 > 0, return total = 4
    getHits(301), valid = 301 - 300 = 1, t=1 invalid, total -= count(1) = 3, return total = 3
5. Time: O(1) for `hit` and O(k) for `getHits`, k number of timestamp;
    Space: O(300), 300:active timestamp
"""
from collections import deque

class HitCounter:

    def __init__(self):
        self.queue = deque()  # (timestamp, num_hits)
        self.total = 0
        

    def hit(self, timestamp: int) -> None:
        if self.queue and self.queue[-1][0] == timestamp:
            self.queue[-1][1] += 1
        else:
            self.queue.append([timestamp, 1])
        self.total += 1


    def getHits(self, timestamp: int) -> int:
        # remove hits with invalid timestamp, t <= current - 300
        while self.queue and self.queue[0][0] <= timestamp - 300:
            _, count = self.queue.popleft()
            self.total -= count
        return self.total


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
