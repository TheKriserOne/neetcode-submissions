class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0

        def dfs(root):
            nonlocal diameter

            if root is None:
                return 0

            a = dfs(root.left)
            b = dfs(root.right)

            diameter = max(diameter, a + b)

            return 1 + max(a, b)

        dfs(root)
        return diameter