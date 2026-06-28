class Solution:

    def encode(self, strs: List[str]) -> str:
        # Encode list of strings to 1 string
        encoded = ""
        for string in strs:
            encoded += str(len(string)) + "@" + string
        print(encoded)
        return encoded

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0 # Start from str start
        while i<len(s):
            j = i # Have these start from the same loc
            while s[j]!='@': # While j not at @ 
                j+=1 # j will be 2 the first time around (with test case 1)
            length = int(s[i:j]) # 0 - 2 (2 excluded, so actuall 1)
            i = j + 1 # 2 + 1 = 3 = start of string
            j = i + length # 3 + 5 = 8 = end of string (+1)
            res.append(s[i:j]) # Actual string - pos 3 to pos 7, 8 excluded
            i = j # Rinse and repeat
        return res
