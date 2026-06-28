class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        prod = 1
        ans = []
        for i in range(n):
            prod = 1
            for j in range(n):
                if i==j:
                    continue
                else:
                    prod=prod * nums[j]
            ans.append(prod)
        return ans