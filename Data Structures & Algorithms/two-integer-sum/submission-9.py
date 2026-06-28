class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # target is an int
        # we want nums[i] + nums[j] == target, i and j unique 
        # return smaller pair first 
        # can't sort since i and j matter 
        # [3, 6, 5, 4], target = 7 
        # [3, 6, 5, 4], target = 11
        # nums[i] + nums[j] = target
        # difference = target - nums[i]
        # So we're looking for something with that difference 
        diffs = {}
        for i, n in enumerate(nums):
            diff = target - n 
            if diff in diffs:
                return [diffs[diff], i]
            diffs[n] = i