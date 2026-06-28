class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # length of longest substring without duplicate characters
        # substring -> contigous sequence
        # longest substring -> maximization aim
        # constraint -> duplicate characters

        # maintain a hashmap
        seen = {}
        l = ans = 0
        for r in range(len(s)):
            seen[s[r]] = seen.get(s[r], 0) + 1
            while seen.get(s[r],0) > 1:
                seen[s[l]] = seen.get(s[l], 0) - 1
                l += 1
            curr = r - l + 1
            if curr > ans:
                ans = curr
        
        return ans


        