class Solution:
    def rob(self, nums: List[int]) -> int:
        # input: nums; nums[i] = money from house i 
        # output: max money
        # constraint: ith house is neighbour to i + 1 and i - 1 houses
        # you cannot rob two adjacent houses -> in essence, starting from 
        # house 0, you can only rob house i+2 or beyond
        if not nums:
            return 0
        if len(nums)==1:
            return nums[0]
        n = len(nums)
        dp = [0] * (n)
        dp[0], dp[1] = nums[0], max(nums[0],nums[1])
        for i in range(2, n):
            dp[i] = max(dp[i-1] ,
                        dp[i-2] + nums[i])
        
        return dp[-1]
        