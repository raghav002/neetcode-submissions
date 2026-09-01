class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # idea is probably add elements till you hit a sign
        # calculate based off sign
        # add that in
        # keep going

        ops = {"+", "-", "*", "/"}
        stack = []
        for t in tokens:
            if t in ops:
                temp2 = int(stack.pop())
                temp1 = int(stack.pop())
                if t=="+":
                    result = temp1 + temp2 
                elif t=="-":
                    result = temp1 - temp2 
                elif t=="*":
                    result = temp1 * temp2 
                else:
                    result = temp1 / temp2 
                stack.append(result)
                print(result)
            else:
                stack.append(t)  
        return int(stack[-1])
        