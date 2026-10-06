class Solution:
    def climbStairs(self, n: int) -> int:
        # input: integer n = number of steps to reach top
        # output: number of distinct ways to climb to the top of the stair case
        # constraint: you can take either 1 or 2 steps at a time

        if n<=2:
            return n
        dp = [0] * (n+1)
        dp[1], dp[2] = 1, 2
        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]
        