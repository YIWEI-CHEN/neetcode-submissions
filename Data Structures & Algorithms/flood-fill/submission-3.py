from collections import deque

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        """
        iterative dfs
        """
        queue = deque()
        origin = image[sr][sc]
        if origin == color:
            return image

        queue.append((sr, sc))
        image[sr][sc] = color
        rows, cols = len(image), len(image[0])

        while queue:
            r, c = queue.popleft()
            for dr, dc in (
                (-1, 0), (1, 0), (0, -1), (0, 1)
            ):
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and image[nr][nc] == origin:
                    queue.append((nr, nc))
                    image[nr][nc] = color
        
        return image
