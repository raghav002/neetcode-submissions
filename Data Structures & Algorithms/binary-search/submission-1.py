class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # nums, ascending order
        # int target
        l = 0
        r = len(nums)-1
        return self.bSearch(nums, target, l, r)

    def bSearch(self, nums, target, l, r):
        if l>r: 
            return -1
        mid = (r+l)//2
        if nums[mid]==target:
            return mid
        elif nums[mid]<target:
            return self.bSearch(nums, target, mid+1, r)
        else:
            return self.bSearch(nums, target, l, mid-1)
