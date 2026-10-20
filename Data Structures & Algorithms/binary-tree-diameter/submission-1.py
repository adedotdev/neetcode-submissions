# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        '''
        DFS
        1. declare a global variable (nonlocal) to track the max diameter
        2. compute the height of the left and right subtrees
        3. 
        '''

        res = 0

        # returns the max height of the tree
        def dfs(node):
            if not node:
                return 0

            leftMax = dfs(node.left)
            rightMax = dfs(node.right)

            nonlocal res
            res = max(res, leftMax + rightMax)
            return 1 + max(leftMax, rightMax)

        dfs(root)
        return res