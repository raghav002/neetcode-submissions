class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        palinCount = n # Each individual element is itself a palin
        palin = s[0]
        for i in range(n):
            j = 1
            currpalin = s[i]
            while i-j>=0 and i+j<n:
                left = i-j
                right =i+j
                if s[right]==s[left]:
                    palinCount+=1
                    j+=1
                else: # means not palindrome, so go to next i 
                    break
        # odd case
        for i in range(n - 1):
            if s[i] != s[i + 1]:
                continue
            palinCount+=1 # if 2 same -> is palin
            currpalin = s[i:i+2]
            j = 1
            leftstart = i
            rightstart = i + 1
            while leftstart - j >= 0 and rightstart + j < n:
                left = leftstart - j
                right = rightstart + j
                if s[left] == s[right]:
                    palinCount+=1
                    j += 1
                else:
                    break
        return palinCount