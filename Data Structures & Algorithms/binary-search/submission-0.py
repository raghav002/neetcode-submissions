class Solution:
    
    def bSearch(self, nums: List[int], target: int, offset: int) -> int:
        midindex = len(nums)//2 
        if not nums:
            return -1
        if nums[midindex]==target:
            return midindex + offset
        elif nums[midindex]<target: # recurse on right half
            return self.bSearch(nums[midindex+1:], target, offset + midindex+1)
        else: # recurse on left half
            return self.bSearch(nums[:midindex], target, offset)

    def search(self, nums: List[int], target: int) -> int:
        # distinct integer array nums, sorted ascendingly
        # int target
        # get target within nums -> return index, or -1
        offset = 0 
        return self.bSearch(nums, target,offset)
        
            
        