class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        top, bottom = 0, ROWS-1
        rowMid = 0
        while top <= bottom:
            rowMid = (top + bottom) // 2
            if matrix[rowMid][0] > target:
                bottom = rowMid - 1
            elif matrix[rowMid][COLS-1] < target:
                top = rowMid + 1
            else:
                break

        left, right = 0, COLS-1
        while left <= right:
            colMid = (left + right) // 2
            if matrix[rowMid][colMid] > target:
                right = colMid - 1
            elif matrix[rowMid][colMid] < target:
                left = colMid + 1
            elif target == matrix[rowMid][colMid]:
                return True

        return False