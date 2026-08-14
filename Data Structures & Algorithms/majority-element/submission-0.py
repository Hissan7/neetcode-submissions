from collections import defaultdict
import math

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums_dict = defaultdict()


        floor_len = len(nums) / 2

        math.floor(floor_len)

        for element in nums:
            if element not in nums_dict:
                nums_dict[element] = 0
            nums_dict[element] += 1 
        print(nums_dict)

        for key in nums_dict.keys():
            if nums_dict[key] > floor_len:
                return key