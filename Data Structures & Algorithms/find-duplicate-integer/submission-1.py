class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # each num is in range [1, n] and we have n+1 numbers
        # this means that we can calculate an index n - curr which will
        # always be within the bound of the array (which goes to 0, n)
        # So for each num we calc an index by doing abs(num) - 1, because
        # the 'bounds' of that index become [0, n-1] which makes sense in
        # context, and we switch the value of that
        # index's sign
        # If this happens to the same index twice, we have a repeated number
        for num in nums:
            ind = abs(num) - 1
            if nums[ind]<0:
                return abs(num)
            nums[ind] *= -1
        return -1