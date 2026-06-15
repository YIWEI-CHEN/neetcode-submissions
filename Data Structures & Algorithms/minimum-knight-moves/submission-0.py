from collections import deque

class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        target_x, target_y = abs(x), abs(y)
        moves = [(1, 2), (2, 1), (2, -1), (1, -2), 
        (-1, -2), (-2, -1), (-2, 1), (-1, 2)]
        
        queue = deque([(0, 0, 0)])
        seen = {(0, 0)}

        while queue:
            curr_x, curr_y, distance = queue.popleft()
            if curr_x == target_x and curr_y == target_y:
                return distance

            for dx, dy in moves:
                nx, ny = curr_x + dx, curr_y + dy
                if (
                    -2 <= nx <= target_x + 2 
                    and -2 <= ny <= target_y + 2
                    and (nx, ny) not in seen
                ):
                    seen.add((nx, ny))
                    queue.append((nx, ny, distance + 1))
        
        return -1

            