class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        curr = []
        candidates.sort()
        def dfs(i = 0, summation = 0):
            if summation == target:
                res.append(curr.copy())   
                return
            elif i > len(candidates) - 1 or summation > target:
                return 
            #left
            curr.append(candidates[i])
            
            dfs(i + 1, summation + candidates[i])
            #right
            curr.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i = i + 1
            dfs(i + 1, summation)
        dfs()
        return res