class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        col_len = len(matrix[0])
        row_len = len(matrix)

        l = 0
        r = row_len * col_len - 1

        while l <= r:
            mid = (l + r) // 2

            row = mid // col_len
            col = mid % col_len

            temp = matrix[row][col]

            if temp > target:
                r = mid - 1
            elif temp < target:
                l = mid + 1
            else:
                return True

        return False


print(
    Solution().searchMatrix(
        [[1,3,5,7],
         [10,11,16,20],
         [23,30,34,60]],
        3
    )
)