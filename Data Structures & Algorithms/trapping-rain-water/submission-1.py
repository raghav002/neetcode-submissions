class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        area = 0
        maxLeft = [0] * n
        maxRight = [0] * n
        maxLeft[0] = height[0]
        for i in range(1, n):
            maxLeft[i] = max(height[i], maxLeft[i-1])
        maxRight[-1] = height[-1]
        for i in range(n-2, -1, -1):
            maxRight[i] = max(height[i], maxRight[i+1])
        for i in range(n):
            area += min(maxLeft[i], maxRight[i]) - height[i]

        print(maxLeft)
        print(maxRight)
        print(height)
        return area
                
        