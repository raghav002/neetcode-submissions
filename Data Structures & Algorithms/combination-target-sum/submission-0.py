class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # input: array of distinct ints nums; target int target
        # output: all unique combinations of nums that sum to target, 
        #         including dupes of the same number
       
        res = []

        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            if i >= len(nums) or total > target:
                return
            cur.append(nums[i])
            dfs(i, cur, total + nums[i])
            cur.pop()
            dfs(i + 1, cur, total)
        dfs(0, [], 0)
        return res
        