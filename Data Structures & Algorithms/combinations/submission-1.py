class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        res = []
        def dfs(index=1, current=[]):
            if len(current) == k:
                res.append(current)
                return
            if k - (len(current) + (n-index)) > 1:
                return
            for i in range(index, n + 1):
                dfs(i + 1, current + [i])
        dfs()
        return res

            





        