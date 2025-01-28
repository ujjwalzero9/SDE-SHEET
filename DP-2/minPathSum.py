#  64. Minimum Path Sum
#  Given a m x n grid filled with non-negative numbers,
#  find a path from top left to bottom right,
#  which minimizes the sum of all numbers along its path.
#  Note: You can only move either down or right at any point in time.

class Solution:
    def minPathSum(self, grid):
        """
        Finds the minimum path sum from the top-left to the bottom-right of a grid.
        Only right and down movements are allowed.
        """
        m = len(grid)
        n = len(grid[0])

        dp = [[0] * n for _ in range(m)]

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if i == m - 1 and j == n - 1:  # Bottom-right corner
                    dp[i][j] = grid[i][j]
                elif i == m - 1:  # Last row
                    dp[i][j] = dp[i][j + 1] + grid[i][j]
                elif j == n - 1:  # Last column
                    dp[i][j] = dp[i + 1][j] + grid[i][j]
                else:  # General case
                    dp[i][j] = grid[i][j] + min(dp[i + 1][j], dp[i][j + 1])

        return dp[0][0]


# Driver Code
if __name__ == "__main__":
    # Example grid
    grid = [
        [1, 3, 1],
        [1, 5, 1],
        [4, 2, 1]
    ]
    
    # Create an instance of Solution
    solution = Solution()
    
    # Find and print the minimum path sum
    result = solution.minPathSum(grid)
    print("Minimum Path Sum:", result)
