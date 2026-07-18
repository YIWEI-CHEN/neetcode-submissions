class Solution:
    def romanToInt(self, s: str) -> int:
        """
        II = 1 + 1
        I V
        1 5
        5 - 1 = 4
        scan s from right to left
        new char smaller than prev max, which tell us substraction
        Time O(n)
        Space O(7) = O(1)
        """

        sym_to_val = {
            "I": 1, "V": 5, "X": 10,
            "L": 50, "C": 100, "D": 500, "M": 1000
        }
        total = 0
        # condition var to sub/add
        max_seen = 0
        for sym in reversed(s):
            val = sym_to_val[sym]
            if val < max_seen:
                total -= val
            else:
                max_seen = val
                total += val
        return total
        