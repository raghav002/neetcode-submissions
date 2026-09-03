# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # input: head - the head of a singly linked-list
        # output: a reordered list (in place), with the elements
        #         reshuffled to [0, n-1, 1, n-2, 2, n-3, ... ]
        
        # We're alternating between the first half of the list in order
        # and the second half of the list in reverse order

        # Separate the list into two by maintaining two pointers
        first = head
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # At this point, slow will be at the midpoint 
        second = slow.next
        slow.next = None # Separates the lists
        # We'll need to reverse the list, so maintain a dummy node with None
        prev = slow.next # Can we do just None? Try it out later
        # Now reverse the second half
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
    
        # Now, starting putting stuff in 
        while prev:
            temp = first.next
            first.next = prev 
            temp2 = prev.next
            prev.next = temp
            prev = temp2
            first = temp
 




        