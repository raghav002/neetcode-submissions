class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Heights[i] = height of ith bar
        # Choose any bar to form container
        # Return max amount of water a container can store
        area = 0
        clen = 0
        n = len(heights)
        l = 0
        r = n -1
        while (l<r):
            clen = r - l
            h = min(heights[l], heights[r])
            currArea = clen*h
            if (currArea>area):
                area = currArea
            if (heights[l]<heights[r]):
                l+=1
            elif (heights[r]<heights[l]):
                r-=1
            else:
                r-=1
        return area
        