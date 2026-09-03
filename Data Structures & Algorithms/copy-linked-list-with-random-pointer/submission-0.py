"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # input: head - beginning of linked list
        # output: deep - a deep copy of the input linked list
        # key constraint: deep copy. Nothing in the copy can point to anything
        #                 in the original 

        # key challenge: When defining a new node, we have to define the next and the
        #                random, which could be in such an order that we'd have to
        #                keep jumping forward to define those, sort of recursion like
        #                we probably could use recursion, but let me see if there's 
        #                a simpler way 

        oldToCopy = {None: None}
        curr = head
        while curr:
            copy = Node(curr.val)
            oldToCopy[curr] = copy
            curr = curr.next
        curr = head
        while curr:
            copy = oldToCopy[curr]
            copy.next = oldToCopy[curr.next]
            copy.random = oldToCopy[curr.random]
            curr = curr.next
        return oldToCopy[head]

        