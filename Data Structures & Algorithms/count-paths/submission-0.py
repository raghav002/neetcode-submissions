class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Can move down or to the right
        # m = rows, n cols
        # number of unique ways you can get to a point will be the sum of
        # the unique ways you can get to the point above it plus the unique
        # ways you can get to the point to its left 
        # dp[i][j] = number of unique ways to reach this point
        # key formula
        # dp[i][j] = dp[i-1][j] + dp[i][j-1]
        # base case: dp[0][0] = 1
        # dp[1][0] = 1; dp[0][1] = 1
        
        dp = [[0] * n for _ in range(m)]
        # populate top and bottom rows first
        for i in range(m):
            dp[i][0] = 1
        for i in range(n):
            dp[0][i] = 1
        # now begin
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[m-1][n-1]
                