class HitCounter:

    def __init__(self):
        self.times = [0] * 300
        self.counts = [0] * 300        

    def hit(self, timestamp: int) -> None:
        i = timestamp % 300
        if self.times[i] == timestamp:
            self.counts[i] += 1
        else:
            self.times[i] = timestamp
            self.counts[i] = 1        

    def getHits(self, timestamp: int) -> int:
        total = 0
        for i in range(300):
            if timestamp - 300 < self.times[i]:
                total += self.counts[i]
        return total
        


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
