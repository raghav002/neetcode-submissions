class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # nums at indexes i, j, and k must add up to 0
        # all such index combinations where 
        # nums[i] + nums[j] + nums[k] == 0 
        # nums[j] + nums[k] == -nums[i]
        nums.sort()
        # Use sorted 2 sum logic
        n = len(nums)
        ans = []
        for i in range(n-2):
            l = i+1
            r = n-1
            target = -nums[i] # 4
            while l<r:
                if target < nums[l] + nums[r]:
                    r-=1
                    continue
                if target > nums[l] + nums[r]:
                    l+=1
                    continue
                if target == nums[l] + nums[r]:
                    if ([nums[i], nums[l], nums[r]] not in ans):
                        ans.append([nums[i], nums[l], nums[r]])
                    r-=1
                    continue
        return ans
        