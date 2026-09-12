class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, maximum):
            if node is None:
                return 0

            return (
                (1 if node.val >= maximum else 0)
                + dfs(node.left, max(node.val, maximum))
                + dfs(node.right, max(node.val, maximum))
            )

        return dfs(root, root.val)