class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s)<len(t):
            return ""

        needed = {}
        for c in t:
            needed[c] = needed.get(c,0) + 1
        need = len(t)
        
        l = 0
        minWindow = 99999999 
        winL, winR = 0, 0
        
        for r in range(len(s)):
            if s[r] in needed:
                if needed[s[r]]>0:
                    need-=1 
                needed[s[r]] -= 1
            while need == 0:
                if r-l+1 < minWindow:
                    minWindow = r-l+1
                    winL, winR = l, r 
                if s[l] in needed:
                    needed[s[l]] = needed.get(s[l],0) + 1
                    if needed[s[l]]>0:
                        need += 1
                l+=1 

        if minWindow == 99999999:
            return ""
        return s[winL:winR+1]
        
        