class Solution:
    def climbStairs(self, n: int) -> int:
        # n = num steps to get to top of stair case
        # Either climb 1 or 2 steps at a time
        # Return number of distinct ways to get to stairs
        # 1D array dp
        # dp[i] = number of ways to move up to ith step
        # 0<i<n
        # dp[i] = dp[i-2] + dp[i-1] 
        # Num ways to get here = 
        # Num ways to get to 2 steps before here + 
        # Num ways to get to 1 step before here
        # Starting cases: dp[0] = 0; dp[1] = 1; dp[2] = 2
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 2
        dp = [0]*(n+1)
        dp[0] = 0
        dp[1] = 1
        dp[2] = 2
        for i in range(3, len(dp)):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]
        