class Solution:
    def isPalindrome(self, s: str) -> bool:
        actstr = "".join([char for char in s if char.isalnum()])
        actstr = actstr.lower()
        r = len(actstr) - 1
        l=0
        while l<=r:
            if actstr[l]!=actstr[r]:
                return False
            l+=1
            r-=1
        return True