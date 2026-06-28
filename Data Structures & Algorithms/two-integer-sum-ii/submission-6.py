class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # input: integer array, non-decreasing order
        # Return indices of numbers that add up to target and where earlier num < later num
        # earlier and later num cannot be the same => cannot use same element twice
        # Only one valid solution always
        # Only O(1) additional space
        # num1 + num2 = target
        # num2 = target - num1
        
        # If array is nondecreasing
        # Start pointers out at either end 
        # If sum is greater than what's needed, reduce from right 
        # If sum is lesser than needed, increase from left
        # Continue until we get the result

        l = 0 
        r = len(numbers) - 1
        while l<r:
            if numbers[l] + numbers[r] > target:
                r-=1
            elif numbers[l] + numbers[r] < target:
                l += 1
            else: 
                return [l+1, r+1]
            
        