
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # input: array nums of unique integers
        # output: all possible subsets of nums
        # constraints: solution set cannot have duplicate subsets. Can return in any order

        res = [[]]
        for num in nums:
            new_subsets = []
            for subset in res:
                new_subsets.append(subset + [num])
            res.extend(new_subsets)
        return res