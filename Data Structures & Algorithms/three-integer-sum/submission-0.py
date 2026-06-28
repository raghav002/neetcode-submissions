class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Condition: nums[i] + nums[j] + nums[k] = 0
        # Rewritten: nums[j] + nums[k] = -nums[i]
        # Return all triplets of this
        # Indices i, j, and k can't be the same
        # Output can't have any duplicate triplets
        # Return the output/triplets in any order

        # First, sort the array (all negatives and positives will be to
        # either side of 0/grouped together)
        nums.sort(); #Ascending order
        n = len(nums)
        ans = []
        # For every i:
        for i in range(n):
            if (i>0 and nums[i]==nums[i-1]):
                continue
            compar = -nums[i]
            j = i+1
            k = n-1
            # Figure out what combo of j and k satisfy eqn in changed form
            while (j<k):
                curSum = nums[j] + nums[k]
                if (curSum>compar):
                    k-=1
                    continue
                if (curSum<compar):
                    j+=1
                    continue
                if (curSum == compar):
                    ans.append([nums[i], nums[j], nums[k]])
                    j+=1
                    k-=1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
        return ans
