class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums[0:len(nums)]) < target:
            print("debug")
            return 0
        # best variable
        shortest_length = float('inf')
        # left window pointer 
        left = 0 
        # sum of nums in window
        window_sum = 0 
        for right in range(0,len(nums)):
            window_sum += nums[right]
            while window_sum >= target:
                shortest_length = min(shortest_length, right - left + 1)
                window_sum -= nums[left]
                left += 1 
        return shortest_length