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
        rows, cols = len(image), len(image[0])
        while queue:
            r, c = queue.popleft()
            if image[r][c] == origin:
                image[r][c] = color
                for dr, dc in (
                    (-1, 0), (1, 0), (0, -1), (0, 1)
                ):
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols:
                        queue.append((nr, nc))
        
        return image
