class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # prices[i] = price of coin on ith day
        # Choose single day to buy one neetcoin, choose diff day
        # in future to sell it 
        # Return maximum profit you can achieve. You can choose
        # to not make any transactions, wherein profit would be 0 
        bday = 0
        sday = 1
        # Overall cond is profit maximization
        maxProf = 0
        # Let's do our first approach which is sort of like a brute force
        n = len(prices)
        while (bday<n):
            sday = bday + 1
            # For each bday, check all possible sdays 
            while (sday!=n):
                currProf = prices[sday] - prices[bday]
                if (currProf>maxProf):
                    maxProf = currProf
                sday+=1
            # After all sdays checked, increase bday and set sday-> bday+1
            bday+=1
            sday = bday+1
        return maxProf

        