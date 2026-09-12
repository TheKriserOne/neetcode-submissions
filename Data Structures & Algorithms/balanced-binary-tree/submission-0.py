# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        balanced = True
        def dfs(root, depth = 0):
            nonlocal balanced
            if root is None:
                return depth

            depth = depth + 1
            a = dfs(root.left, depth)
            b = dfs(root.right, depth)
            if abs(a-b) > 1:
                balanced = False
            depth = max(a,b)
            return depth
        dfs(root)
        return balanced
        
