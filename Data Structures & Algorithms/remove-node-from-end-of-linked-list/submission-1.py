# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Remove nth node from the END of the list + return list
        # Given the head and the integer
        # Have 2 pointers in some sense - first and second
        # Removing nth from the end is same as removing N - nth from the start
        # Have first move up n steps first
        # Have second at the beginning
        # Move both together until first hits null
        # Second will be right at point before node to be removed due to dsit
        # property
        # Remove
        dummy = ListNode(0, head)
        first = head
        second = dummy
        for i in range(n):
            first = first.next
        while first:
            first = first.next
            second = second.next
        second.next = second.next.next
        return dummy.next









