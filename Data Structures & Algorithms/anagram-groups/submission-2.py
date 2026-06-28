class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        keys = {}
        for word in strs:
            newKey = [0]*26
            for c in word:
                cval = ord(c) - 97
                newKey[cval]+=1
                #print(ord('a')-97)
            stringedKey = str(newKey)
            if stringedKey not in keys:
                keys[stringedKey] = [word]
            else:
                keys[stringedKey].append(word)
        return list(keys.values())

        