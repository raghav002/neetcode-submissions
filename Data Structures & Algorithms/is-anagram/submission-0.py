class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sHM = {}
        for char in s:
            sHM[char] = sHM.get(char, 0) + 1
        for char in t:
            if char in sHM:
                sHM[char]-=1
                if sHM[char]==0:
                    sHM.pop(char)
        return len(sHM)==0
        
        

        