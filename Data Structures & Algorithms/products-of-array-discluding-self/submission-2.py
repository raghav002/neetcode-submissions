class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # If there's a single 0 anywhere, that means the product for everything
        # else except those 0s is 0. Only for those 0s will the prod be totprod
        
        n = len(nums)
        pref = [0]*n
        suf = [0]*n
        res = [0]*n
        pref[0] = suf[n-1] = 1
        for i in range(1,n):
            pref[i] = pref[i-1] * nums[i-1]
        for i in range(n-2, -1, -1):
            suf[i] = suf[i+1] * nums[i+1]
        for i in range(n):
            res[i] = pref[i] * suf[i]
        return res

        # O(n^2) soln:
        """
        n=len(nums)
        prod = 1
        ans = []
        for i in range(n): # O(n)
            prod = 1
            for j in range(n): # n - 1 times, O(n) 
                if i==j:
                    continue
                else:
                    prod=prod * nums[j]
            ans.append(prod)
        return ans
        """