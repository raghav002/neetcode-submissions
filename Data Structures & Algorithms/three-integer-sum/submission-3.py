class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Input: interger array nums
        # output: All triplets, excluding duplicates, and in any order
        #         where nums[i] + nums[j] + nums[k] = 0
        #         Alt: -nums[i] = nums[j] + nums[k]

        # Since it doesn't care about order, we'll sort the array in ascending order
        # iterate through nums for each i 
        # At each i, start pointers l and r at i+1 and len(nums) - 1
        # Do the two sum method of non-decreasing array until you reach an answer for -nums[i]
        # Add it to the set
        # Go to next i 
        # return set 
        nums.sort()
        ans = []
        n = len(nums)
        for i in range(n-2):
            if i >0 and nums[i]==nums[i-1]:
                continue
            target = -nums[i]
            l, r = i+1, n-1
            while l<r:
                curr = nums[l] + nums[r]
                if curr>target:
                    r-=1
                elif curr<target:
                    l+=1
                elif curr == target:
                    ans.append([nums[i], nums[l], nums[r]])
                    while l<r and nums[l]==nums[l+1]:
                        l+=1
                    while l<r and nums[r] == nums[r-1]:
                        r-=1
                    l+=1
                    r-=1
        return ans
        