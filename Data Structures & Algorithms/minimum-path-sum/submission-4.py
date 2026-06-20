class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        """
            1. min sum from upper or left cell.
                dp[r][c] = grid[r][c] + min(grid[r - 1][c], grid[r][c - 1])
            2. we don't change grid, so we need array for memoization. 1-D array is enough 
            since dp just needs upper and left cells and current dp prior to being updated holds previous values.
            3. init dp[0:c] with first row of grid
            4. before updating dp[c], dp[c - 1] is left cell, dp[c] is upper cell.
                dp[c] = grid[r][c] + min(dp[c - 1], dp[c])
        """
        rows, cols = len(grid), len(grid[0])
        dp = grid[0][:]  # copy first row of grid

        # init dp
        for c in range(1, cols):
            dp[c] = dp[c - 1] + grid[0][c]  # only can move right in first row
        
        for r in range(1, rows):
            dp[0] += grid[r][0]  # from row 1, we can move down. dp is the min val of current row
            for c in range(1, cols):
                # dp[c - 1] holds min from left, dp[c] holds min from upper
                dp[c] = grid[r][c] + min(dp[c - 1], dp[c])
        
        return dp[-1]