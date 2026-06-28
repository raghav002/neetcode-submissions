class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        diffdict = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in diffdict:
                return [diffdict[diff], i]
            diffdict[num] = i
        # 
        # Brute force
        #for i in range(n):
         #   for j in range(n):
          #      if i!=j:
           #         if nums[i] + nums[j] == target:
            #            return [i, j]


        