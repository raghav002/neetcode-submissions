class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # buy, sell
        b, s = 0, 1
        maxP = 0
        n = len(prices)
        while (s<n):
            #First, start comparing prices
            if (prices[b]<prices[s]):
                p = prices[s]-prices[b]
                maxP = max(maxP, p)
            else:
                b = s
            s+=1
        return maxP
