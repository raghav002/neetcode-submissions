class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Return length of max consecutive sub array (doesn't have to exist
        # consecutively within the original array)
        numset = set(nums)
        longest = 0
        for num in numset:
            if (num-1) not in numset:
                length = 1
                while (num+length) in numset:
                    length+=1
                longest = max(length, longest)
        return longest
        