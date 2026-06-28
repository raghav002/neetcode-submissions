class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # two strings -> s and t
        # If anagrams, return true
        # Anagram = word containing exact same letters, including letter count
        #           order diff
        # Method: Use hashmap 
        chars = {}
        for c in s:
            chars[c] = chars.get(c,0) + 1
        for c in t:
            if c not in chars:
                return False
            if c in chars:
                chars[c] -= 1
            if chars[c] == 0:
                del chars[c]
        if len(chars) > 0:
            return False
        print(chars)
        return True

        