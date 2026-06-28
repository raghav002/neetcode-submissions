class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Palindrome = same letters backward and forward
        nospaces = "".join(char for char in s if char.isalnum()).lower()
        n = len(nospaces)-1
        l = 0
        while l<=n:
            if nospaces[l]!=nospaces[n]:
                return False
            l+=1
            n-=1
        return True