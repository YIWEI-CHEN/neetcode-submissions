from heapq import heappop, heappush

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        """
        step 1: restate & clarify
        intervals [start, end]
        queries
        output - shortest length of intervals that contain each query, ie start <= query <= end
        length = end - start + 1
        no interval -> length = -1
        confirm 1 interval overlap freely 2. and queries are arbritrary integers?
        step 2: brute force and key observations
        brute force approach O(n * q), n = |intervals|; q = |queries| 
        handle queries in any order
        sort queries, process small to large, --> a single foward scan, no repeating scanning
        [[1,3],[2,3],[3,7],[6,6]], query 1, 2, 3
        for 1, [1, 3]
        for 2, [1, 3], [2, 3]
        for 3, [1, 3], [2, 3], [3, 7]
        step 3: my plan
        1. sort intervals by start
        2. sort queries with their original index
        3. min heap (length, end).
            3.1 add interval to heap if eligible for the query, start <= current query
            3.2 remove intervals, whose end < query, query only increase, that interval is not used again
            3.3 if heap, head heap is the ans
        step 4: time/space
        1. sort interval O(nlogn); sort queries O(qlogq) = O((n+q)logn)
        2. heap O((n+q)logn) = overall O((n+q)logn)
        3. space: O(n + q)
        step 5: writing code
        """
        heap = []
        i = 0
        ans = [-1] * len(queries)
        intervals.sort()
        sorted_queries = sorted((query, idx) for idx, query in enumerate(queries))
        for query, idx in sorted_queries:
            while i < len(intervals) and intervals[i][0] <= query:
                start, end = intervals[i]
                heappush(heap, (end - start + 1, end))
                i += 1
            while heap and heap[0][1] < query:
                heappop(heap)
            
            if heap:
                ans[idx] = heap[0][0]

        return ans