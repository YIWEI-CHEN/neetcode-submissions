from collections import Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """
        [A, A, A, B, C], n=2
        A _ _ A _ _ A
          B C
        | _ _ |     |
         n + 1      max_count
        1. greedy, optimal: most freq tasks (f)
        2. f - 1 blocks, take n + 1 units, max_count (tasks sharing the max freq)
        3. fram length = (f - 1) blocks * (n + 1) unit + max_count
        4. edge cases
           [A, A, B, C, D], n = 2
           exec order  A B C D A -> len(tasks) = 5
        """
        # count = {
        #   A: 3, B: 1, C:1
        # }
        counts = Counter(tasks)
        max_freq = max(counts.values())
        """
        [A, A, B, B]
        A:2, B:2, n=2
        A _ _ A 
          B     B
              | |
               max count
        """
        max_count = sum(1 for count in counts.values() if count == max_freq)
        frame = (max_freq - 1) * (n + 1) + max_count

        # edge case, len(tasks)
        return max(len(tasks), frame)
