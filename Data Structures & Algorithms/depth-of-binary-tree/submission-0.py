# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(root, maximum = 0):
            if root is None:
                return maximum
            maximum = maximum + 1
            a = dfs(root.left, maximum)
            b = dfs(root.right, maximum)
            maximum = max(a,b)
            return maximum
        return dfs(root)




        