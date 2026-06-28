class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # cost[i] = cost of taking step from ith floor, up to either i+1th
        # or i+2th floor
        # You can start at index 0 or 1 floor
        # return min cost to reach top of staircase/past last index in cost
        # We will always start at min (cost1, cost0)
        # The minimum to leave a specific floor i is 
        # dp[i] = min(dp[i-1], dp[i-2]) + cost[i]
        # Min cost between the two possibilites i-1 and i-2, + its own cost

        n = len(cost)
        dp = [0]*(n)
        dp[0] = cost[0]
        dp[1] = cost[1]
        for i in range(2, len(dp)):
            dp[i] = min(dp[i-1], dp[i-2]) + cost[i]
        return min(dp[n-2], dp[n-1])
        