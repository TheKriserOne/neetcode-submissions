class Solution:
    def isSameTree(self, p: TreeNode | None, q: TreeNode | None) -> bool:
        res = []
        res2 = []
        def dfs(node,res):
            if node is None:
                res.append(None)
                return None

            res.append(node.val)
            dfs(node.left, res) 
            dfs(node.right, res)
        dfs(p,res)
        dfs(q, res2)
        return res == res2
        