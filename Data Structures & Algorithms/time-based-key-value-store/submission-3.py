from collections import defaultdict
from bisect import bisect_right

class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        versions = self.store[key]
        if not versions:
            return ""
        i = bisect_right(versions, timestamp, key=lambda x: x[0]) - 1
        return "" if i < 0 else versions[i][1]
