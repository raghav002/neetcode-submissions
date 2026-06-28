class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        l = 0 
        r = n-1
        maxcon = -1
        while l<r:
            possans = (r-l)*min(heights[l], heights[r])
            if possans > maxcon:
                maxcon = possans
            if heights[l]<heights[r]:
                l+=1
            else:
                r-=1
        return maxcon