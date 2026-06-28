class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Longest substring of s that is a palindrome
        # If multiple of same length, read same forward and backward
        n = len(s)
        maxLen = 1
        palin = s[0]
        for i in range(n):
            # For each i, try expanding to the left and right
            j = 1
            currLen = 1
            currpalin = s[i]
            while i-j>=0 and i+j<n:
                left = i-j
                right =i+j
                if s[right]==s[left]:
                    currLen+=2
                    currpalin = s[left:right+1]
                    j+=1
                else: # means not palindrome, so go to next i 
                    break
            if currLen > maxLen:
                maxLen = currLen
                palin = currpalin
        # odd case
        for i in range(n - 1):
            if s[i] != s[i + 1]:
                continue
            currLen = 2
            currpalin = s[i:i+2]
            j = 1
            leftstart = i
            rightstart = i + 1
            while leftstart - j >= 0 and rightstart + j < n:
                left = leftstart - j
                right = rightstart + j
                if s[left] == s[right]:
                    currLen += 2
                    currpalin = s[left:right+1]
                    j += 1
                else:
                    break
            if currLen > maxLen:
                maxLen = currLen
                palin = currpalin
        return palin
        
        