# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        '''
        1. use a dummy node to enable reversal and kth node retrieval
        2. get kth node using a helper function
        3. perform reversal in k-group:
            - initialize prev, curr = kth.next, groupPrev.next
        4. after each k-group reversal:
            - the node that groupPrev points to becomes the new 'tail'
            - and the kth node always needs to become the new head of that group
            - therefore adjust groupPrev (the node before the group ie dummy) to point to the kth node
            - and update groupPrev to point to the original first node in the group (which now becomes the node before the next k-group)
        5. return the head of the new linked list (dummy.next)
        '''

        dummy = ListNode(0, head)
        groupPrev = dummy

        while True:
            kth = self.getKth(groupPrev, k)
            if not kth:
                break
            groupNext = kth.next

            prev, curr = kth.next, groupPrev.next
            while curr != groupNext:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp

            tmp = groupPrev.next
            groupPrev.next = kth
            groupPrev = tmp
        return dummy.next
            

    def getKth(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr