class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        p1 = 0
        p2 = len(numbers)-1
        ans1 = -1
        ans2 = -1
        while (p1!=p2):
            if (numbers[p1]+numbers[p2]<target):
                # Gotta increase p1
                p1+=1
                continue
            if (numbers[p1]+numbers[p2]>target):
                # Gotta reduce p2
                p2-=1
                continue
            if (numbers[p1]+numbers[p2]==target):
                ans1 = p1+1
                ans2 = p2+1
                break
        return [ans1, ans2]
            
