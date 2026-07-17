class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # input: int array nums
        # output: int array output 
        # output[i] = product of all nums except nums[i]

        prod, zeros = 1, 0
        for num in nums:
            if num!=0:
                prod*=num
            else:
                zeros+=1
        output = [0]*len(nums)
        if zeros>1:
            return output
        elif zeros == 1:
            for i in range(len(nums)):
                if nums[i]!=0:
                    output[i]==0
                else:
                    output[i] = prod
            return output
        else: 
            # O(n) time without division op
            # calc prefix array (with prefix[i] excluding nums[i])
            # calc suffix array (with suffix[i] excluding nums[i])
            # output[i] would hence be prefix[i] * suffix[i]
            prefix = [0]*len(nums)
            prefix[0] = 1
            preprod = 1
            suffix = [0]*len(nums)
            suffix[-1] = 1
            sufprod = 1
            for i in range(1, len(prefix)):
                prefix[i] = prefix[i-1] * nums[i-1] 
            for i in range(len(suffix)-2, 0, -1):
                suffix[i] = suffix[i+1] * nums[i+1]
            for i in range(len(nums)):
                output[i] = prod//nums[i]
            return output
            