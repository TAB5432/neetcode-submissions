class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        
        rows = len(matrix)
        cols = len(matrix[0])

        l, r = 0, (rows * cols) - 1

        while l <= r:
            m = (l+r) // 2
            mid_val = matrix[m // cols][m % cols]

            if target > mid_val:
                l = m+1
            elif target < mid_val:
                r=m-1
            else:
                return True
        
        return False
