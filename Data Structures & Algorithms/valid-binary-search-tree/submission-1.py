class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        stack = []
        node = root
        res = []
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            res.append(node.val)
            if len(res) > 1 and res[-1] <= res[-2]:
                return False
            node = node.right
        return True
             