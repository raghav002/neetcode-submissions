class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        dp = [-1]*(amount + 1)
        dp[0] = 0
        for i in range(1, len(dp)):
            currmin = 100000
            for c in coins:
                if (i-c>=0) and dp[i-c]>=0:
                    temp = dp[i-c] + 1
                    if temp < currmin:
                        currmin = temp
            if currmin != 100000:
                dp[i] = currmin
            else:
                dp[i] = -1
        return dp[amount]
                    
        
        