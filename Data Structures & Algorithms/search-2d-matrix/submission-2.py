class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # input: m x n 2d int array, int target 
        # output: true if target exists in the matrix, false otherwise
        # constraints: 
        # 1) O(log(m*n)) time
        # 2) Each row is in non-decreasing order (dupes can exist)
        # 3) First int of each row greater than last integer of previous row

        # Constraint on output probably means that we want to check both horizontal and vertical axis in log time
        # This can be done with binary search. Initially, the left and right windows will start from the extremes available
        # We check across the row first. If the target is lower than the right edge, it's a simple binary search here
        # and we return
        # If it's not in this row, we check in the column. If the middle values across the middle row's middle column 
        # of the current 'window' is less than the target, we check in the columns below this midpoint. Same case
        # for rows

        rowLen = len(matrix[0])
        colLen = len(matrix)

        left, right = 0, colLen * rowLen

        while left<right:
            mid = (right-left) // 2 + left
            row = mid // rowLen 
            col = mid % rowLen 
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                left = mid + 1
            else:
                right = mid 
        return False




        