from heapq import heappop, heappush

class MedianFinder:

    def __init__(self):
        self.lo, self.hi = [], []

    def addNum(self, num: int) -> None:
        if not self.lo or num <= -self.lo[0]:
            heappush(self.lo, -num)
        else:
            heappush(self.hi, num)
        
        if len(self.lo) > len(self.hi) + 1:
            heappush(self.hi, -heappop(self.lo))
        elif len(self.hi) > len(self.lo):
            heappush(self.lo, -heappop(self.hi))

    def findMedian(self) -> float:
        if len(self.lo) > len(self.hi):
            return -self.lo[0]
        return (-self.lo[0] + self.hi[0]) / 2
        