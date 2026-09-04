class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # input: array of ints containing n+1 ints, range [1, n]
        # output: repeated integer, of which there is only 1
        # constraints: no modification of nums
        #              O(1) extra space
        # Easiest way would be to sort it and then find the first instance
        # of repeat, but that would be O(nlogn) and would be modifying the 
        # array
        # We probably can't make a hashmap frequency count either, since 
        # even though that's not modifying the array, that would take up
        # O(n) space in the worst case
        # Even a set approach wouldn't work cuz that would still be O(n) 
        # extra space. Lets do it for now though and see

        seen = set()
        ans = float('inf')
        for i in range(len(nums)):
            if nums[i] in seen:
                ans = nums[i]
            else:
                seen.add(nums[i])
        return ans
        