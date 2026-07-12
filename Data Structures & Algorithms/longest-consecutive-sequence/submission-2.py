class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # input: nums, an array of ints
        # output: length of the longest consecutive sequence of elements that can be formed
        # constraints: each element in sequence has to be exactly 1 greater than the previous
        # elements do not have to be consecutive in the original array 
        # i.e. -> 2, 3, 5, 4, 6 -> the longest is 5 because you can rearrange them to 2,3,4,5,6

        seen = set()
        visited = set()
        poss = 0
        ans = 0
        for num in nums:
            seen.add(num)
        for num in nums:
            curr = num
            if curr-1 not in seen:
                while curr in seen and curr not in visited:
                    visited.add(curr)
                    poss += 1
                    curr+=1  
                ans = max(ans, poss)
                poss = 0 
        return ans
        