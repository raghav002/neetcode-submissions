class Solution:
    def trap(self, height: List[int]) -> int:
        # non-neg ints height = elevation map 
        # height[i] = height of bar, width 1
        # return max area of water trappable between all bars
        # Max water trappable at a bar =
        # min(maxLeftBarHeight, maxRightBarHeight) - this bar height
        n = len(height)
        maxLefts = [0]*n
        maxRights = [0]*n
        maxLeft = -1
        maxRight = -1
        for i in range(n):
            if height[i]>maxLeft:
                maxLeft = height[i]
                maxLefts[i] = maxLeft
            else:
                maxLefts[i] = maxLeft
        i = n-1
        while i>0:
            if height[i]>maxRight:
                maxRight = height[i]
                maxRights[i] = maxRight
                i-=1
                continue
            else:
                maxRights[i] = maxRight
                i-=1 
                continue
        print(maxLefts)
        print(maxRights)
        sum = 0
        for i in range(n):
            temp = min(maxLefts[i], maxRights[i]) - height[i]
            if temp>=0:
                sum+=temp
        return sum