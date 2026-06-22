class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        """
        1. directions: up, down, left, right with the same color of the origin
        2. need to remember original color
        3. process: check above/below/left/right pixel color, same -> change color and put adjancts to dfs
        4. recursive approach 
        5. time: O(rows*cols), space O(rows*cols)
        """
        origin = image[sr][sc]
        # source color is the new color, no pixel is updated
        if color == origin:
            return image
        
        rows, cols = len(image), len(image[0])
        def dfs(r, c):
            # boundary
            if r < 0 or r == rows or c < 0 or c == cols or image[r][c] != origin:
                return
            image[r][c] = color
            dfs(r - 1, c)
            dfs(r + 1, c)
            dfs(r, c - 1)
            dfs(r, c + 1)
        
        dfs(sr, sc)
        return image
        