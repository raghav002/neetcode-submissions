class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)>len(t):
            return False
        tmap = {}
        for c in t:
            tmap[c] = tmap.get(c, 0) + 1
        for c in s:
            if c in tmap:
                tmap[c] = tmap.get(c,0) - 1
                if tmap[c] == 0:
                    del tmap[c]
        if len(tmap)>0:
            return False
        else:
            return True
        