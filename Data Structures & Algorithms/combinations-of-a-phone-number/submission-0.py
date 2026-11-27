class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        dic = {
            2: "abc",
            3: "def",
            4: "ghi",
            5: "jkl",
            6: "mno",
            7: "pqrs",
            8: "tuv",
            9: "wxyz",
        }

        def dfs(index=0):
            if index == len(digits):
                return []
            previous = dfs(index + 1)
            new = []
            for i in range(len(dic[int(digits[index])])):
                if previous:
                    for j in previous:
                        new.append(dic[int(digits[index])][i] + j)
                else:
                    new.append(dic[int(digits[index])][i])
            return new

        res = dfs()
        return res
