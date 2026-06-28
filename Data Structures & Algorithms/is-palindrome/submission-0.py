class Solution:
    def isPalindrome(self, s: str) -> bool:
        p1 = 0;
        p2 = len(s)-1
        while (p1<p2):
            # Check if alphanumeric
            if (s[p1].isalnum()==False):
                # Increase index by one
                p1+=1
                continue
            if (s[p2].isalnum()==False):
                p2-=1
                continue
            # Second check to ensure p1<p2
            if (s[p1].lower() != s[p2].lower()):
                return False
            p1+=1
            p2-=1
        return True
        