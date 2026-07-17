class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # input: int array nums
        # output: int array output 
        # output[i] = product of all nums except nums[i]

        # let's do what we think first
        # simple approach: calculate product of all elements
        # except 0 elements. Then iterate through the nums,
        # and we have the following cases:
        # if no 0s, straight forward
        # if 1 0, straight forward
        # if 2 or more 0s, straight forward - all products will be 0

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
            for i in range(len(nums)):
                output[i] = prod//nums[i]
            return output
            