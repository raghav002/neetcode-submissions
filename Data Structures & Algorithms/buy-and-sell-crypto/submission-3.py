class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # int array prices -> prices[i] = price of coin on ith day
        # choose one day to buy, a day >i to sell
        # return max profit 
        # can choose to not make any transactions 
        # key idea: maximize prices[j] - prices[i]
        # brute force, check every combo 
        # let's do brute force first
        max = 0
        n = len(prices)
        for i in range(n):
            for j in range(i+1, n):
                if prices[j] - prices[i] > max:
                    max = prices[j] - prices[i]
        return max

        