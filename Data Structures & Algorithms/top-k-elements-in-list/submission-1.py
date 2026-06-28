class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Return top k most frequent elements in an array
        # Just sort array, descending order, and return the first two 
        # elements (unique)
        #nums.sort(reverse=True)
        n = len(nums)
        ans = []
        numsHM = {}
        for num in nums:
            if num not in numsHM:
                numsHM[num] = numsHM.get(num, 0) + 1
            else:
                numsHM[num]+=1
        while k>0:
            maxNum = max(numsHM, key=numsHM.get)
            ans.append(maxNum)
            numsHM[maxNum]=0
            k-=1
        return ans