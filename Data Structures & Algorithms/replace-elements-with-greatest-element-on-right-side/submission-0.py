class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:

        for i in range(0,len(arr)-1):
            max_from_right = max(arr[i+1:len(arr)])
            arr[i] = max_from_right
        arr[-1] = -1
        
        return arr
        