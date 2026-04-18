class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        total_rows = len(matrix)
        total_cols =  len(matrix[0])

        top = 0
        down = total_rows * total_cols - 1   

        # now we have our mid we need it in our 2d array matrix

        while top <= down:
            mid = top + (down - top) // 2
            r = mid // total_cols 
            c = mid % total_cols

            if matrix[r][c] < target:
                top = mid + 1 
            elif matrix[r][c] > target:
                down = mid - 1
            else:
                return True
        return False

    


        # 4x4 = 16 we have 16 units but if we implement this as a 1D array that means we'll have 15 elements 
        # top, down = 0, 4*4 - 1 = 15  
        # total rows = 4
        # total cols = 4 
        # mid = 0 + (15 + 0) // 2 = 7 
        # r = 7 // 4 = 1
        # c = 7 % 4 = 3 
        # 1 < 3 
        # 
    
            


#[[0,1,2,3],[4,5,6,7]]

#2x4 







        