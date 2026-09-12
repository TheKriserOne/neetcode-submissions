
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        res = []
        if not root:
            return res

        q = [root]
        while q:
            level = []
            current = []
            for node in q:
                level.append(node.val)
                if node.left:
                    current.append(node.left)
                if node.right:
                    current.append(node.right)

            res.append(level)
            q = current

        return res