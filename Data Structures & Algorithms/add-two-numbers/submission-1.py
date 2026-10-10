# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        temp = ListNode(0)
        curr = temp

        # l1 != None and l2 != None
        # l1 == None or l2 == None
        # !(l1 == None and l2 == None)
        # l1 != None or l2 != None
        # while l1 has a node or l2 has a node (while either of them still has a node)
        while l1 != None or l2 != None:
            sum  = temp.val
            if l1 != None:
                sum += l1.val
                l1 = l1.next
            
            if l2 != None:
                sum += l2.val
                l2 = l2.next
            
            quotient, remainder = sum // 10, sum % 10
            temp.val = quotient
            curr.next = ListNode(remainder)
            curr = curr.next
        
        curr.next = ListNode(1) if temp.val > 0 else None
        return temp.next
