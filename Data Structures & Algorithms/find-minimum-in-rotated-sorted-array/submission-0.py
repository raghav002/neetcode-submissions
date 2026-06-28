class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
        mid = len(nums)//2
        while l<r:
            mid = (l + r -1)//2
            if nums[mid]<nums[r]: # if middle less than r, min is somewhere left
                r = mid
            else: # nums[mid]>nums[r]
                l = mid + 1
        return nums[l]