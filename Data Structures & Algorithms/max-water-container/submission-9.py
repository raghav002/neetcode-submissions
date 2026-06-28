class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # input: an integer array representing towers of height i 
        # output: the maximum amount of water a container can store given two edges l, r
        # constraint: we want to maximize the value of (r-l) * min(height[l], height[r])
        # implied constraint: the lower of the two heights will always be the deciding factor

        l = 0
        r = len(heights) - 1
        maxH = 0
        while l<r:
            curr = (r-l) * min(heights[l], heights[r])
            maxH = max(maxH, curr)
            if heights[l]<heights[r]:
                l+=1
            elif heights[l]>heights[r]:
                r-=1
            else:
                l+=1
                r-=1
        return maxH

        