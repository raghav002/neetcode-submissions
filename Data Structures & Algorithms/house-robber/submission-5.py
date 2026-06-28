class Solution:
    def rob(self, nums: List[int]) -> int:
        # nums[i] = amount of money house i has
        # houses arranged in straight line -> i is neighbour of i+1, i-1
        # Want to rob money, but cannot rob two adjacent houses 
        # Return max money you can rob without alerting the police 
        # Recurrence
        # dp[i] = max((dp[i-2] + nums[i]), dp[i-1])
        # The max between two choices - robbing this house i, meaning you have
        # to consider dp[i-2], or not robbing this house i, meanign we consider
        # dp[i-1]
        n = len(nums) # num houses 
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        dp = [0]*n
        dp[0] = nums[0] # Starting from house 0 
        dp[1] = max(nums[0], nums[1]) # Starting from house 1 (in reality, we still
                                       #  would rob house 0 and go on from there if it had better profitability)
        if n == 2:
            return max(dp)
        for i in range(2, len(dp)):
            dp[i] = max((dp[i-2] + nums[i]), dp[i-1])
        return dp[n-1]