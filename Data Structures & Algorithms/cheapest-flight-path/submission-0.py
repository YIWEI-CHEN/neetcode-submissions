class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        INF = float("inf")
        dist = [INF] * n
        dist[src] = 0

        for _ in range(k + 1):
            nxt = dist[:]
            for u, v, w in flights:
                if dist[u] != INF and dist[u] + w < nxt[v]:
                    nxt[v] = dist[u] + w
            dist = nxt
        
        return -1 if dist[dst] == INF else dist[dst]