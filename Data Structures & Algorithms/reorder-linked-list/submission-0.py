# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Head of singly linked list
        # If indices are as follows
        # 0 1 2 3 4 5 6
        # We want
        # 0, n-1, 1, n-2, 2, n-3, ... 
        # n = 7 in the above case 
        # Must reorder nodes themselves 
        # This can be separated up
        # First, find the midpoint of the list. Then, reverse the linked list after that point
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        # Reverse the right half of list
        # [0 1 2 3 -> 4 -> 5 -> 6 -> NULL]
        # [0 1 2 3 6 5 4 -> NULL]
        revstart = slow.next
        slow.next = None # terminates the first half of list 
        prev = None # 3
        curr = revstart # 4
        while curr != None:
            temp = curr.next # 5
            curr.next = prev # 4 -> 3
            prev = curr
            curr = temp
        # [0(head), 1, 2, 3] [6 (prev), 5, 4]
        new = head
        while new and prev:
            temp = new.next # 1
            new.next = prev # 0->6
            temp2 = prev.next
            prev.next = temp # 6->1
            prev = temp2 # 5
            new = temp
        ans = head
        print(ans)

        