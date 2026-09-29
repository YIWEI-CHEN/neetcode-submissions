from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        counts = 0
        seen = set()

        for r in range(rows):
            for c in range(cols):
                if (r, c) in seen or grid[r][c] != "1":
                    continue
                counts += 1
                queue = deque([(r, c)])
                while queue:
                    x, y = queue.popleft()
                    for dx, dy in ((-1, 0), (1, 0), (0, 1), (0, -1)):
                        nx, ny = x + dx, y + dy
                        if (
                            0 <= nx < rows and 0 <= ny < cols 
                            and (nx, ny) not in seen and grid[nx][ny] == "1"
                        ):
                            queue.append((nx, ny))
                            seen.add((nx, ny))

        return counts
        