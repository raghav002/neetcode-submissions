class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # input: ascending distinct integer array nums; an int target
        # output: index of target's existence in nums, -1 if it doesn't exist
        # constraint: must be in O(logn) time

        # set ans to -1 first

        ans = -1

        # what is the base case? Or rather when this algorithm stops?
        # since its binary search, when the left and right bounds are the same
        l = 0
        r = len(nums) - 1
        while l<=r:
            # 0, 5
            # mid = 2
            # nums[mid] = 2
            mid = ((r - l) // 2) + l 
            if nums[mid] == target:
                ans = mid
                break
            elif nums[mid] < target:
                # recurse on right half
                l = mid+1
            else:
                # recurse on left half
                r = mid-1


        return ans
        