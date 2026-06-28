class Solution:
    def rob(self, nums: List[int]) -> int:
        # nums[i] = profit from robbing house 0 
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])
        dp = [0]*(n-1) # exclude last house
        dp[0] = nums[0]
        dp[1] = max(nums[1], nums[0])
        for i in range(2, len(dp)):
            dp[i] = max((dp[i-2] + nums[i]), dp[i-1])
        
        dp2 = [0]*(n-1) # exclude first house
        dp2[0] = nums[1] # nums[0] not considered
        dp2[1] = max(nums[1], nums[2])
        for i in range(2, len(dp2)):
            dp2[i] = max((dp2[i-2] + nums[i+1]), dp2[i-1])
        return max(dp[n-2], dp2[n-2])