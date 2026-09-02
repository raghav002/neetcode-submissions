class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # input: two int arrays - position and speed. the ith value of both indicates
        #                         the position and speed of the ith car respectively
        # output: the number of sets of cars that are driving at the same position 
        #         and same speed that will arrive at the destination 
        # constraints: a car cannot pass a car ahead of it. It can only match its
        #              speed and destination at that point 

        stats = [0]*len(position)
        for i in range(len(position)):
            stats[i] = [position[i], speed[i]]
        stats.sort(reverse=True)
        stack = []
        for i in range(len(position)):
            stack.append((target - stats[i][0]) / stats[i][1])
            if len(stack)>=2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)
        