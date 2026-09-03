# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # input: head - the beginning of a linked list
        #        n    - an integer
        # output: the linked list with the node that is n away from the end removed

        # Let's do a 2 pointers approach. One will be the head, the other will be 
        # n ahead of the head (might change to n-1, let's see)
        dummy = ListNode(None, head)
        first = dummy
        second = head
        while n>0:
            second = second.next
            n -= 1
        while second:
            first = first.next
            second = second.next
        first.next = first.next.next
        print(first.val) 
        return dummy.next
        