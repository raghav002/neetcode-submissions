class Solution:
    def findMin(self, nums: List[int]) -> int:
        # input: array of length n, originally sorted in ascending order
        #        it is rotated between 1 to n times
        #        a rotation of k moves the k last elements to the beginning
        #        a rotation of n gives you the exact same array
        #        all members of nums are unique
        # output: the minimum element of the array on O(logn) time

        l, r = 0, len(nums)-1
        while l<r:
            mid = (l + r) // 2
            if nums[mid] > nums[r]: # to the right of mid
                l = mid + 1
            else:
                r = mid
        return nums[l]

        