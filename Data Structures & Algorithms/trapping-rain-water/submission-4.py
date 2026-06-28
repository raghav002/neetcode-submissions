class Solution:
    def trap(self, height: List[int]) -> int:
        maxLeft = [height[0]]
        n = len(height)
        mL = 0
        maxRight = [0]*(n)
        maxRight[n-1] = height[n-1]
        mR = 0
        
        for i in range(n):
            maxLeft.append(max(maxLeft[-1], height[i]))
        print(maxLeft)
        counter = n-1
        while counter>-1:
            maxRight[counter] = max(height[counter], mR)
            if mR<height[counter]:
                mR = height[counter]
            counter-=1
        print(maxRight)
        tot = 0
        for i in range(n):
            if maxLeft[i]>0 and maxRight[i]>0 and height[i]<min(maxLeft[i], maxRight[i]):
                tot = tot + min(maxRight[i], maxLeft[i]) - height[i]
                print(tot)
            else:
                continue
        return tot


        