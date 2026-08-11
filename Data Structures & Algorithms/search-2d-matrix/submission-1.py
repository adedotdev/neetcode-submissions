class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        top, bottom = 0, ROWS-1
        midRow = 0
        while top <= bottom:
            midRow = (top + bottom) // 2
            if target < matrix[midRow][0]:          # first element in the row being searched
                bottom = midRow - 1
            elif target > matrix[midRow][COLS-1]:     # last element in the row being searched
                top = midRow + 1
            else:
                break

        left, right = 0, COLS-1
        while left <= right:
            midCol = (left + right) // 2
            if target < matrix[midRow][midCol]:
                right = midCol - 1
            elif target > matrix[midRow][midCol]:
                left = midCol + 1
            elif target == matrix[midRow][midCol]:
                return True

        return False