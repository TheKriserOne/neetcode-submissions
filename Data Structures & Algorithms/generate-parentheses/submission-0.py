class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        res = []
        def dfs(parenthesis, left = 0, right = 0):
            if right > left:
                return
            if left == n and right == n:
                res.append(parenthesis)
            if left < n:
                # parenthesis = parenthesis + "("
                # left += 1
                dfs(parenthesis + "(", left + 1, right)
            if right < n:
                # parenthesis = parenthesis + ")"
                # right += 1
                dfs(parenthesis + ")", left, right + 1)
        dfs("")
        return res

                
            


        