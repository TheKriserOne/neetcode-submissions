# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        q = [root]
        visible = [root.val]
        while q:
            isVisible = True
            next = []
            for node in q:       
                if node.right:  
                    next.append(node.right)
                    if isVisible:
                        visible.append(node.right.val)
                        isVisible = False
                if node.left:
                    next.append(node.left)
                    if isVisible:
                        visible.append(node.left.val)
                        isVisible = False
                
                
            q = next
        return visible
                    
            


                    

        

        