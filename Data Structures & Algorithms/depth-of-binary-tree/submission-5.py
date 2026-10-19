# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        maxDepth = 0

        def dfs(node):
            if not node:
                return 0
            currDepth = max(dfs(node.left), dfs(node.right))
            return 1 + currDepth
        
        maxDepth = dfs(root)
        return maxDepth