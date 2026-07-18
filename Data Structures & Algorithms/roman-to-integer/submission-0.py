class Solution:
    def romanToInt(self, s: str) -> int:
        sym_to_val = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        total = 0
        max_seen = 0
        for c in reversed(s):
            val = sym_to_val[c]
            if val < max_seen:
                total -= val
            else:
                total += val
                max_seen = val
        return total

