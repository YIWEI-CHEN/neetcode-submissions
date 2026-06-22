class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        """
        1. remember origin color to avoid recursive
        2. recursive approach
        """
        origin = image[sr][sc]
        if origin == color:
            return image

        rows, cols = len(image), len(image[0])
        
        def dfs(r, c):
            if r < 0 or r == rows or c < 0 or c == cols or image[r][c] != origin:
                return
            
            image[r][c] = color
            dfs(r - 1, c)
            dfs(r + 1, c)
            dfs(r, c - 1)
            dfs(r, c + 1)

        dfs(sr, sc)

        return image
