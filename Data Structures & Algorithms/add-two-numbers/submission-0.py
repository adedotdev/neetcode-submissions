# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        '''
        temp node?
        1. declare a new linked list to hold the resulting numbers
        2. use a temp head to hold the carrying 1 if present and curr to keep track of each addition
        3. iterate through both lists simultaneously using their respective heads (l1 & l2)
            - if at least one of the lists' head is not null, keep iterating (while not (l1 == None and l2 == None))
            - check each list's head is not null and add the value at it's current position to the sum
            - using the sum as the dividend and 10 as the divisor, retrieve the quotient (q = sum // 10) and the remainder (r = sum % 10)
            - assign the remainder to a new node and the quotient (1 or 0) to the temp node
        4. return the head of the new linked list (temp.next)
        '''

        temp = ListNode(0)
        curr = temp

        while not (l1 == None and l2 == None):
            sum = temp.val
            if l1 != None:
                sum += l1.val
                l1 = l1.next

            if l2 != None:
                sum += l2.val
                l2 = l2.next

            temp.val = sum // 10
            curr.next = ListNode(sum % 10)
            curr = curr.next

        if temp.val == 1:
            curr.next = ListNode(1)

        return temp.next