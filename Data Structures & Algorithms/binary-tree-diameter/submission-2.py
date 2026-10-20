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
        2. traverse the tree using a helper that returns the max height (or max depth) of the tree
        3. for each root node:
            - compute the height of its left and right subtrees
            - add the height of the child subtrees to get the diameter at that node (leftMax + rightMax)
            - compare the current max diameter with the diameter at that node and keep whichever's greater
            - return the max height of the two child subtrees + the current node
        4. return the result
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