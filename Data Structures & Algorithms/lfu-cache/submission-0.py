from collections import defaultdict, OrderedDict

class LFUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.kv, self.cnt = {}, {}
        self.buckets = defaultdict(OrderedDict)
        self.minf = 0

    def _touch(self, key):
        c = self.cnt[key]
        del self.buckets[c][key]
        if not self.buckets[c]:
            del self.buckets[c]
            if self.minf == c:
                self.minf = c + 1
        self.cnt[key] = c + 1
        self.buckets[c + 1][key] = None


    def get(self, key: int) -> int:
        if key not in self.kv:
            return -1
        self._touch(key)
        return self.kv[key]

    def put(self, key: int, value: int) -> None:
        if key in self.kv:
            self.kv[key] = value
            self._touch(key)
            return
        if len(self.kv) == self.cap:
            old, _ = self.buckets[self.minf].popitem(last=False)
            if not self.buckets[self.minf]:
                del self.buckets[self.minf]
            del self.kv[old], self.cnt[old]
        self.kv[key] = value
        self.cnt[key] = 1
        self.buckets[1][key] = None
        self.minf = 1


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)