class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        diffdict = {}
        for i, num in enumerate(nums):
            diff = target - num # Get the difference between this num and target
            if diff in diffdict: # If its already present, means we have a number s.t. 
                                 # that plus nums[i] = target
                return [diffdict[diff], i] # Return value ass with the diff (the prev 
                                           # index), and this i
                # Technically it's probably possible that you have multiple differences, but the 
                # algorithm structure ensures you take the earliest one
            diffdict[num] = i # If it's not there, store this difference's assoced index
        # 
        # Brute force
        #for i in range(n):
         #   for j in range(n):
          #      if i!=j:
           #         if nums[i] + nums[j] == target:
            #            return [i, j]


        