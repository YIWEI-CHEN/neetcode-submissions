class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def need_days(cap):
            d, curr = 1, 0
            for w in weights:
                if curr + w > cap:
                    d += 1
                    curr = 0
                curr += w
            return d
        
        lo, hi = max(weights), sum(weights)
        while lo < hi:
            mid = (lo + hi) // 2
            if need_days(mid) <= days:
                hi = mid
            else:
                lo = mid + 1
        return lo