class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Return true if any value appears more than once 
        # Method: Use set to check for duplicates
        seen = set()
        for num in nums:
            if num not in seen:
                seen.add(num)
            else:
                return True
        return False
        