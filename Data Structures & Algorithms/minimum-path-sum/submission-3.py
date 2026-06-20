class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        """
        1. valid directions: right and down
        2. cells are >= 0, current min is from prev top or prev left
            dp[r][c] = grid[r][c] + min(dp[r-1][c], dp[r][c-1])
        3. if we do not change grid, we need to have 1-D arr, dp[0:c-1] 
           to remember current min. Before updating dp[c], dp[c-1] hold the previous row vals
        4. if we change grid, we just save current min to grid[r][c]
        """
        # use (3) to implement
        rows, cols = len(grid), len(grid[0])
        dp = grid[0][:] # copy first row

        # init dp
        for c in range(1, cols):
            dp[c] += dp[c - 1]
        
        for r in range(1, rows):
            dp[0] += grid[r][0] # the most left from upper row
            for c in range(1, cols):
                dp[c] = grid[r][c] + min(dp[c], dp[c - 1])

        return dp[-1]




