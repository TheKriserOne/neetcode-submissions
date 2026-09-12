# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if root is None:
            return 0
        good = 0
        def dfs(root, maximum = root.val):
            nonlocal good
            if root is None:
                return maximum  
            if root.val >= maximum:
                good += 1
            maximum = max(maximum, root.val)
            dfs(root.left, maximum)
            dfs(root.right, maximum)
        dfs(root)
        return good



        