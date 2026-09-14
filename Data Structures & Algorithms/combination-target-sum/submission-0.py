class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        curr = []
        def dfs(i = 0):
            foo = sum(curr)
            if foo == target:
                res.append(curr.copy())
                return
            elif i > len(candidates) - 1 or foo > target:
                return 

            #left
            curr.append(candidates[i])
            dfs(i)
            
            #right
            curr.pop()
            dfs(i + 1)
        
        dfs()
        return res