class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # target = numbers[index1] + numbers[index2]
        l = 0
        r = len(numbers) - 1
        while l<=r:
            if target < numbers[l] + numbers[r]: # sum too large
                r -= 1
                continue
            if target > numbers[l] + numbers[r]: # sum too small
                l += 1
                continue
            if target == numbers[l] + numbers[r]:
                return [l+1, r+1]
        return [-1, -1]