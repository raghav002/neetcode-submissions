class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # input: int array piles; piles[i] = num banans in ith pile
        #        int h = num of hours available to eat all the banans
        # output: minimum banans/hour eating rate k s.t. you can eat all in h
        # constraints: Each hour, choose a pile of banans and eat k banas from it
        #              if it had less than k banans before you start eating it, you 
        #              finish the pile but cannot eat another pile IN THE SAME hour
        
        # Key points: MINIMUM k 
        # Key points: piles.length <= h 
        # This implies the upper bound for the answer is sum(piles)/h

        # I think this thing is suggest we look at the max bound of k, then 
        # keep decreasing by 1 from there so long as the thing is met?

        l, r = 1, max(piles)
        ans = r
        while l<=r:
            k = (l+r)//2
            totTime = 0
            for pile in piles:
                totTime += math.ceil(float(pile)/k)
            if totTime<=h:
                ans = k 
                r = k - 1
            else:
                l = k + 1
        return ans