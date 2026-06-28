class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #price[i] = price on ith day
        # choose one day to buy one, and a day after it in the future to sell it
        # return MAX PROFIT you can achieve. You can choose not to do any transactions
        # brute force method: go to ith day, check every jth day after that
        minPrice = 1000000
        profit = 0
        ans = 0 
        for r in range(len(prices)):
            if prices[r]<minPrice:
                minPrice = prices[r]
            profit = prices[r]-minPrice
            if profit>ans:
                ans = profit
        return ans
        