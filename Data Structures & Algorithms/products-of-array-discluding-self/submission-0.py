class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        result = len(nums) * [0]
        prefix_arr = (len(nums)+1) * [1] #[1,1,1,1,1,1] [1,2,3,4,5]
        suffix_arr = (len(nums)+1) * [1] #[1,1,1,1,1,1]
        for i in range(1,len(nums)+1):
            prefix_arr[i] = prefix_arr[i-1] * nums[i-1]
        print(f"prefix arr : {prefix_arr}")
        for j in range(len(nums)-1,-1,-1):
            suffix_arr[j] = nums[j] * suffix_arr[j+1]
        print(f"suffix arr : {suffix_arr}")
        for k in range(len(nums)):
            result[k] = prefix_arr[k] * suffix_arr[k + 1]
        return result