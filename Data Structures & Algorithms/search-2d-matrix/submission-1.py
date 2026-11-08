class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    
        rows_high = len(matrix) - 1
        rows_low = 0
        found_row = False
        
        while rows_low <= rows_high and found_row == False:
            mid = (rows_low + rows_high)//2
            print(matrix[mid])
            if matrix[mid][0] > target:
                rows_high = mid - 1
            elif matrix[mid][-1] < target:
                rows_low = mid + 1
            else:
                found_row = True
                row = matrix[mid]
        if not found_row:
            
            return False
        
        high = len(row) - 1
        low = 0

        while low <= high:
            mid = (low + high)//2
            if row[mid] > target:
                high = mid - 1
            elif row[mid] < target:
                low = mid + 1
            else:
                return True
        return False


    

