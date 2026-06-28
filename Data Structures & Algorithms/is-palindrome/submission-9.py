class Solution:
    def isPalindrome(self, s: str) -> bool:
        # input: string; output: boolean
        # constraint: input must be a palindrome. case-insensitive, non-alphanumeric ignored
        conv = s.lower()
        n = len(conv)
        l = 0
        r = n - 1
        while l < r:
            while l < r and not conv[l].isalnum():  
                l += 1
            while l < r and not conv[r].isalnum(): 
                r -= 1
            if conv[l] != conv[r]:
                return False
            l += 1
            r -= 1
        return True
        