from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.times = defaultdict(list)
        self.vals = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.times[key].append(timestamp)
        self.vals[key].append(value)

    def get(self, key: str, timestamp: int) -> str:
        times = self.times[key]
        if not times:
            return ""
        
        idx = self.bisect_right(times, timestamp) - 1
        return "" if idx < 0 else self.vals[key][idx]

    def bisect_right(self, a, x):
        lo, hi = 0, len(a)
        while lo < hi:
            mid = (lo + hi) // 2
            if x < a[mid]:
                hi = mid
            else:
                lo = mid + 1
        return lo
