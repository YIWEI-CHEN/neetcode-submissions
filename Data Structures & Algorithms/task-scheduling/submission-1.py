from collections import Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """
        X, X, Y, Y, n = 2
        greedy, most freq task
        X _ _ X
          1 2 3 => n + 1 units 
          2 - 1 => f - 1 blocks
          Y     Y
              | | => no wait units, chunk, sharing max freq, max counts
        A, A, B, C, D
        A _ _ A
          B C
        A B C D A => len(tasks)
        Time: O(T)
        Space: O(26) = O(1)
        """
        counts = Counter(tasks)
        max_freq = max(counts.values())
        max_count = sum(1 for count in counts.values() if count == max_freq)
        frame = (max_freq - 1) * (n + 1) + max_count

        return max(len(tasks), frame)

