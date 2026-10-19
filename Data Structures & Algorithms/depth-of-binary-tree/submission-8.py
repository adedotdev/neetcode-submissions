# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        '''
        DFS
        1. for each valid node:
            - compute the max of the left subtree and max of the right subtree
        2. do this recursively

        time: O(n)
        space: O(h)
        where n is the number of nodes in the tree and h is the height of the tree
        '''
        
        if not root:
            return 0

        leftMax = self.maxDepth(root.left)
        rightMax = self.maxDepth(root.right) 
        return 1 + max(leftMax, rightMax)