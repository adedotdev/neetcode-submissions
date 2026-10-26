# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        '''
        divide and conquer
        1. iterate through the list of LLs with a step of 2 (ie 0, 2, 4...):
            - for each step, using a helper function, merge the current LL and the LL to be skipped
            - append the new LL formed after each merge to a new temp list (merged)
        2. assign the list of merged lists to the original list
        3. repeat this process while the size of the list is greater than 1
        4. return the resulting list

        time: O(n)
        space: O(1)
        '''

        if not lists or len(lists) == 0:
            return None

        while len(lists) > 1:
            merged = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i+1] if i+1 < len(lists) else None
                merged.append(self.mergeLists(l1, l2))
            lists = merged
        return lists[0]

    def mergeLists(self, l1, l2):
        temp = ListNode()
        curr = temp
        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
        
        curr.next = l1 if l1 else l2
        return temp.next
            