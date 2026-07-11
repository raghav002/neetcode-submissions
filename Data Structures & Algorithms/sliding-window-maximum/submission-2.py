class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # Input: int array nums and integer k 
        # Sliding window of size k starting at left edge
        # Window slides to right until reaching right edge
        # Return a list that contains maximum element in the window at each step    

        heap = []
        ans = []
        for i in range(len(nums)):
            heapq.heappush(heap, (-nums[i], i))
            if i>= k - 1:
                while heap[0][1] <= i-k:
                    heapq.heappop(heap)
                ans.append(-heap[0][0])
        return ans 
        