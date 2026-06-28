class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # If there are no zeroes, no problem
        # If there is one zero -> Everything except that zero has a zero prod
                                # and that zero has a normal prod
        # If there are 2 zeroes -> Everything has a 0 prod 
        zerocount = 0
        totprod = 1
        for num in nums:
            if num==0:
                zerocount+=1
            if num!=0:
                totprod *= num
        if zerocount>1:
            return [0]*len(nums)
        res = []
        if zerocount==1:
            for num in nums:
                if num!=0:
                    res.append(0)
                else:
                    res.append(totprod)
        if zerocount==0:
            for num in nums:
                temp = totprod
                res.append(temp//num)
        return res