# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        d = [[]]
        d[0].append(root.val)
        def bfs(root, depth = 1):
            nonlocal d 
            if root is None:
                return
            if root.left:
                if depth > len(d) - 1:
                    d.append([])
                d[depth].append(root.left.val)
            if root.right:
                if depth > len(d) - 1:
                    d.append([])
                d[depth].append(root.right.val)
        
            bfs(root.left, depth + 1)
            bfs(root.right, depth + 1)
            return root
        bfs(root)
        return d
      
            
            

        