# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # input: head, the beginning of a linked list
        # output: true if there's a cycle, false if there isn't
        # imp fact: if cycle, the tail will point to the ith node where i is the 
        #           start of the cycle. If no cycle, tail will point to null 
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
        