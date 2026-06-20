class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        """
            1. min sum from left cell and upper cell
                dp[r][c] = grid[r][c] + min(dp[r - 1][c], dp[r][c - 1])
            2. We can change grid, we update dp in the grid
                grid[r][c] = grid[r][c] + min(grid[r - 1][c], grid[r][c - 1])
        """
        rows, cols = len(grid), len(grid[0])
        for r in range(rows):
            for c in range(cols):
                if r == 0 and c == 0:
                    continue  # init
                elif r == 0: 
                    # move right, dp from left cell
                    grid[r][c] += grid[r][c - 1]
                elif c == 0:
                    # move down, dp from above cell
                    grid[r][c] += grid[r - 1][c]
                else:
                    grid[r][c] += min(grid[r][c - 1], grid[r - 1][c])
        
        return grid[-1][-1]
                