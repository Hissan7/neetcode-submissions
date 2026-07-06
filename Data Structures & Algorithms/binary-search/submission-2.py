class Solution:
    def search(self, nums: list[int], target: int,) -> int:
        print(nums)
        left = 0 
        right = len(nums)-1
        while left <= right:
            mid = (left+right)//2 
            #print(f"mid is {mid} which is element {nums[mid]}")
            if target < nums[mid]:
                right = mid -1 
                #print(f"target is less than nums[mid] ({target} < {nums[mid]}) right pointer is now {right} which is the element {nums[right]}")
            elif target > nums[mid]:
                left = mid + 1
                #print(f"target is more than nums[mid] ({target} > {nums[mid]}) left pointer is now {left} which is the element {nums[left]}")
            elif target == nums[mid]:
                return mid
        return -1 