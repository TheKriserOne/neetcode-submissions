class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        row_len = len(board)
        col_len = len(board[0])

        def dfs(y, x, index, visited):
            # Current cell does not match
            if board[y][x] != word[index]:
                return False

            # We matched the last character
            if index == len(word) - 1:
                return True

            visited[y][x] = True

            # right
            if x < col_len - 1 and not visited[y][x + 1]:
                if dfs(y, x + 1, index + 1, visited):
                    return True

            # down
            if y < row_len - 1 and not visited[y + 1][x]:
                if dfs(y + 1, x, index + 1, visited):
                    return True

            # left
            if x > 0 and not visited[y][x - 1]:
                if dfs(y, x - 1, index + 1, visited):
                    return True

            # up
            if y > 0 and not visited[y - 1][x]:
                if dfs(y - 1, x, index + 1, visited):
                    return True

            # Backtrack: allow this cell to be used by another path
            visited[y][x] = False

            return False

        for y in range(row_len):
            for x in range(col_len):
                visited = [
                    [False] * col_len
                    for _ in range(row_len)
                ]

                if dfs(y, x, 0, visited):
                    return True

        return False