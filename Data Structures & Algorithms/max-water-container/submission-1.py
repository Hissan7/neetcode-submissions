class Solution:
    def maxArea(self,heights: list[int]) -> int:
        print(heights)
        best_area = 0 
        left = 0 #start pointer
        right = len(heights)-1 #end pointer
        while left < right:
            width = right - left #find width
            height = min(heights[left],heights[right]) 
            current_area = width * height 
            if current_area > best_area:
                best_area = current_area
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1      
        return best_area