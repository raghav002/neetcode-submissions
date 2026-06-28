class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # input: uppercase english word s, k letter replacements
        # goal: MAXIMIZE longest substring
        # constraint: only one distinct character in substring
        # freedom: can replace up to k letters 
        counts = {}
        l = maxf = 0
        res = 0
        for r in range(len(s)):
            counts[s[r]] = 1 + counts.get(s[r], 0)
            maxf = max(maxf, counts.get(s[r], 0))
            while (r-l+1) - maxf > k:
                counts[s[l]]-=1
                l+=1
            res = max(res, r-l+1)
        return res