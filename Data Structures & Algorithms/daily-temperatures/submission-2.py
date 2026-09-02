class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # input: array of int temps, temperatures, i representing temp on ith day
        # output: results where results[i] is number of days after ith day until 
        #         a warmer temperature appears. 0 if none 
        # key constraint: for every i, we have to figure out the next temps[i] that
        #                 is greater

        # Maintain a stack of INDICES. Wherever the incoming indice value is greater,
        # it's greater than all previous indices. Then, just calculate results[i]
        # based off those values
        
        stack = []
        res = [0] * len(temperatures)
        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][1]:
                stackInd, stackT = stack.pop()
                res[stackInd] = i - stackInd
            stack.append((i, t))
        return res

        