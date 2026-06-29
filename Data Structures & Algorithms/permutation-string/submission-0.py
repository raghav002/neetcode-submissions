class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Input: 2 strings -> s1, s2
        # Output: true or false
        # Condition: If s2 contains a permutation of s1
        # Otherwords: if s1 is a subset of s2 

        # Put all of s1 into a hash map, with freq counts
        # Iterate through s2, and decrease counts as you go by, remove if at 0
        # If the hash map size is greater than zero, return false

        if len(s1)>len(s2):
            return False
        freq = [0] * 26
        for c in s1:
            freq[ord(c)-97]+=1
        n1 = len(s1)
        r = 0
        freq2 = [0] * 26
        for i in range(n1):
            freq2[ord(s2[i])-97]+=1
        l = 0 
        if freq == freq2:
            return True
        else:
            for i in range(n1, len(s2)):
                freq2[ord(s2[i])-97]+=1
                freq2[ord(s2[l])-97]-=1
                l+=1
                if freq == freq2:
                    return True
        return False
        