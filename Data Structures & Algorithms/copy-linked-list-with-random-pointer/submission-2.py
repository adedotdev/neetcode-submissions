"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        deepCopy = {None:None}

        curr = head
        while curr:
            deepCopy[curr] = Node(curr.val)
            curr = curr.next

        curr = head
        while curr:
            copy = deepCopy[curr]
            copy.next = deepCopy[curr.next]
            copy.random = deepCopy[curr.random]
            curr = curr.next

        return deepCopy[head]