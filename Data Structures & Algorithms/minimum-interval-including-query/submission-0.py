from heapq import heappop, heappush

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        sorted_queries = sorted((q, i) for i, q in enumerate(queries))
        i = 0
        heap = []
        ans = [-1] * len(queries)

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



        