# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        first = list1
        sec = list2
        dummy = ListNode()
        curr = dummy
        test = True
        while test:
            if (first!=None) and (sec!=None):
                if (first.val<=sec.val):
                    curr.next = first
                    first=first.next
                    curr = curr.next
                    continue
                elif (sec.val<first.val):
                    curr.next = sec
                    sec = sec.next
                    curr = curr.next
                    continue
            elif (first == None) and (sec != None):
                curr.next = sec
                sec=sec.next
                curr=curr.next
                continue
            elif (first != None) and (sec == None):
                curr.next = first
                first=first.next
                curr=curr.next
                continue
            elif (first==None) and (sec==None):
                test = False
        return dummy.next
        