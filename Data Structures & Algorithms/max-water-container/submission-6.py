class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # array
        # heights[i] = height of ith bar 
        # choose two bars l, r to form a container
        # return max water a container can store
        # storage = (r - l)*min(heights[l], heights[r])
        # Let's try this out - store bar to either side of each container
        n = len(heights)
        left = [0]*n
        right = [0]*n
        leftmax = -1
        rightmax = -1
        for i in range(n):
            if heights[i]>leftmax:
                leftmax = heights[i]
                left[i] = leftmax
            else:
                left[i] = leftmax
        i = n-1
        while n>0:
            if heights[n-1]>rightmax:
                rightmax = heights[n-1]
                right[i] = rightmax
                n-=1
                i-=1
                continue
            else:
                right[i] = rightmax
                n-=1
                i-=1
                continue
        maxcon = -1
        interval = [-1, -1]
        for i in range(len(left)):
            l = i 
            r = i+1
            while r<len(left):
                possans = (r-l)*min(heights[l], heights[r])
                if possans>maxcon:
                    maxcon = possans
                    interval[0]=l
                    interval[1]=r
                r+=1
        return maxcon
        