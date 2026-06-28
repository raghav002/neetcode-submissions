# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # index beginning of cycle, if it exists
        # tail of list has its next pointer to the ith indexed node
        # index doesn't actually exist as something we can check
        curr = head
        visited = set()
        while curr != None:
            if curr not in visited:
                visited.add(curr)
                curr = curr.next
                continue
            else:
                return True
        return False
        