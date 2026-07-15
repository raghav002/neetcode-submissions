class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # input: array of strings strs
        # output: anagrams grouped into sublists, any order
        # constraint: anagram = one string has the exact same chars of another, but order is different

        # We'll use a hashmap where the key is a 26-char array indicating frequency counts of 
        # characters, and values are the strings for strs that match those character counts

        seen = {}
        for string in strs:
            temp = [0]*26
            for c in string:
                temp[ord(c)-97] +=1
            if "".join(str(temp)) in seen:
                seen["".join(str(temp))].append(string)
            else:
                seen["".join(str(temp))] = [string]        
        return list(seen.values())
                