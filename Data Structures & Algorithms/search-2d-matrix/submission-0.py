class Solution:
    def searchMatrix(self,matrix: list[list[int]], target: int, left = 0, right = None) -> bool:

        found = False 

        # how many rows 
        m = len(matrix)

        # how many cols 
        n = len(matrix[0])

        # assigning right pointer 
        if right is None:
            right = (m * n) - 1 

        # base case
        if left > right:
            return False 

        # midpoint calculation 
        mid = (left + right) // 2 

        row = mid // n
        col = mid % n

        # if the midpoint is equal to the target then found is true 
        if matrix[row][col] == target:
            found = True
            return found
        elif matrix[row][col] < target:
            return self.searchMatrix(matrix,target,mid+1,right)
        elif matrix[row][col] > target:
            return self.searchMatrix(matrix,target,left,mid-1)
        return found 


            