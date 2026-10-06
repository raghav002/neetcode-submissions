class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # input: array of ints cost; cost[i] = cost of taking step FROM step i 
        # output: return min cost to reach top of staircase, past last index in cost
        # constraint: after paying cost, can go to i+1th or i+2th floor 
        # constraint: can start at index 1

        # At each step, we have two choices - we pay cost and go to step i+1 or i+2
        # Generally, we want to take the minimum of these 
        # The cost of having reached the current step i (before leaving) is the
        # cheapest between coming here from i-1 or i-2
        # tot[i] = min(tot[i-1] + tot[i-2]) And we keep calcing that?
        n = len(cost)
        tot = [0] * (n+1)
        tot[0] = cost[0]
        tot[1] = cost[1]
        for i in range(2, n+1):
            if i<=n-1:
                tot[i] = min(tot[i-1], tot[i-2]) + cost[i]
            else:
                tot[i] = min(tot[i-1], tot[i-2])
        print(*tot, sep= ", ")
        return tot[-1]
        