from collections import deque
class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        # first quadrant solution can be applicable to others
        target_x, target_y = abs(x), abs(y)
        moves = [
            (1, 2), (2, 1), (2, -1), (1, -2),
            (-1, 2), (-2, 1), (-2, -1), (-1, -2)
        ]
        # boundary
        # [-2, x + 2], [-2, y + 2]
        
        # memorize which coordinates have been visited
        seen = {(0, 0)}

        # BFS, cur_x, cur_y, distance
        queue = deque([(0, 0, 0)])

        while queue:
            cur_x, cur_y, distance = queue.popleft()
            if cur_x == target_x and cur_y == target_y:
                return distance
            
            for dx, dy in moves:
                nx, ny = cur_x + dx, cur_y + dy
                if (
                    -2 <= nx <= target_x + 2
                    and -2 <= ny <= target_y + 2
                    and (nx, ny) not in seen
                ):
                    seen.add((nx, ny))
                    queue.append((nx, ny, distance + 1))
        
        return -1

