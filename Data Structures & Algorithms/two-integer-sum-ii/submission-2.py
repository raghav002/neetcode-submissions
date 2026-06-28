class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # nums sorted in non-decreasing order (always increases or stays same)
        # return indexes that add up to given target number with i1 < i2
        # numbers[i] + numbers[j] = target
        # diff = target - numbers[i]
        diffs = defaultdict(int)
        for i, n in enumerate(numbers):
            diff = target - n
            if diff in diffs:
                return [diffs[diff]+1, i+1]
            diffs[n] = i