class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        """
        dp[r][c] = grid[r][c] + min(dp[r][c-1], dp[r-1][c])
        """
        rows, cols = len(grid), len(grid[0])

        for r in range(rows):
            for c in range(cols):
                if r == 0 and c == 0:
                    continue
                elif c == 0:
                    grid[r][c] += grid[r - 1][c]
                elif r == 0:
                    grid[r][c] += grid[r][c - 1]
                else:
                    grid[r][c] += min(grid[r][c-1], grid[r-1][c])

        return grid[-1][-1]

