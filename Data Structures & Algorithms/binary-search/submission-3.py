class Solution:
    def search(self,nums: list[int], target: int, left = 0, right = None) -> int:
        if right is None:
            right = len(nums)-1
        #base case
        if left > right:
            return -1
        mid = (left+right)//2 
        if target < nums[mid]:
            return self.search(nums,target,left,mid-1)
        elif target > nums[mid]:
            return self.search(nums,target,mid+1,right)
        elif target == nums[mid]:
            return mid
        return -1  