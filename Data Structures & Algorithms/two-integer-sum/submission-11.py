class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # input: integer array nums, int target
        # output: indicies i and j according to the condition
        # condition: nums[i] + nums[j] = target, i!=j
        # how can we rewrite the condition?
        # nums[j] = target - nums[i]
        # so j needs to be an indice meeting the above

        # At every iteration through nums, we make a note of the value of the current 
        # this will be nums[i]
        # We then calculate target-nums[i] to say "this number i needs this value j"
        # We add the value of i as a key to a hashmap, and map to it the value of j 
        # We check on the next iteration (assuming we were just on the first) if 
        # this curr value is in the .values() of the hashmap
        # we then check if this index has the same value as the associated key
        # If both these conditions are met, we have our answer

        seen = {}
        for i, num in enumerate(nums):
            if num in seen:
                return [seen[num], i]
            seen[target-num] = i 
        return [0, 0]
        