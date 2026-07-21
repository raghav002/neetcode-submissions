class Solution:
    def findMin(self, nums: List[int]) -> int:
        # input: array of length n, originally sorted in ascending order
        #        it is rotated between 1 to n times
        #        a rotation of k moves the k last elements to the beginning
        #        a rotation of n gives you the exact same array
        #        all members of nums are unique
        # output: the minimum element of the array on O(logn) time

        # when we rotate the array by k, we are essentially changing the indices of all the elements as so:
        # newIndex = currIndex + k (wrapping around when it goes beyond n)
        # If we have an element at indice 2 and rorate the array 4 times
        # it goes to indice 0, assuming n is of length 6
        # 2 -> 3 -> 4 -> 5 -> 6 (0)
        # An element at indice 4 would go to 2
        # 4 -> 5 -> 0 -> 1 -> 2
        # An element at indice i would go to 
        # (i + k) % n 

        # We're trying to find the minimum here, so the bounds of binary search won't be based off index 
        # Let's say we first get what the first and last elements are
        start = nums[0]
        end = nums[-1]
        l, r = 0, len(nums)
        # If start < end, this means we have a classic binary search case 
        # If start > end, this means we have had a rotation 
        # If start > end, what does that mean? It means the minimum is somewhere in between the two of them still
        # Let's see what the 'mid' is. We get mid.
        # If start < mid, what does that mean? It means the answer is somewhere on the right 
        # If start > mid, what does that mean? It means the answer is somewhere on the left. We would also store this value as the least for now
        # If mid < end, what does that mean? It means the answer is either that mid, or somewhere on the left
        # If mid > end, what does that mean? It means the answer is somewhere on the right 
        # I believe we only need to use one of the above cases. Let's start out with the start and mid comparison 
        ans = 100000
        if start > end:
            while l<r:
                mid = ( l + r ) // 2
                print(mid)
                if start < nums[mid]: # answer on the right
                    l = mid + 1
                else: # answer on the left, but store this answer for now
                    r = mid
                    ans = min(ans, nums[mid])
        else:
            ans = start
        return ans

        