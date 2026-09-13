# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root: 
            return True
        stack = []
        def dfs(root):
            nonlocal stack
            if root is None:
                return 
            a = dfs(root.left)
            stack.append(root.val)
            b = dfs(root.right)

            return
        dfs(root)
        for index, val in enumerate(stack):
            if index >= 1 and val <= stack[index - 1]:
                return False
        return True


            
                
            
            

            
            

        


        

                



        