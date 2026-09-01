class Solution:
    def isValid(self, s: str) -> bool:
        # given s containing brackets
        # output true/false if s is 'valid'
        # validity: if every open bracket has a corresponding close bracket
        # if every open bracket is closed in the correct order (no out of order closing)
        # every close bracket has a corresponding open bracket
        hM = {')': '(', '}': '{', ']': '['}
        stack = []
        for c in s:
            if c in hM:
                if stack and stack[-1] == hM[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
            
        return True if not stack else False
        