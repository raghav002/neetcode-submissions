class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # input: int array nums, int k 
        # output: k most frequest elements in array
        # approach:
        # sort all the numbers first, then start a sliding window at the start
        # enlarge window until the next element is not the window element
        # store as 'key:value' the number and its window's associated length
        # At the end, sort the hashmap by greatest values and return the top k 
        # ones
        
        count = {}
        for num in nums:
            count[num] = count.get(num,0) + 1
        
        arr = []
        for num, cnt in count.items():
            arr.append([cnt,num])
        arr.sort()

        res = []
        while len(res)<k:
            res.append(arr.pop()[1])
        return res
        