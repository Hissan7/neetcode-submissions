class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        final_result = []
        """
        returns a list of lists 

        so for this problem we need to return a list of lists, where the sublists contain triplets that add up to 0 

        "Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] where nums[i] + nums[j] + nums[k] == 0, and the indices i, j and k are all distinct."

        """
        nums.sort() #sort the array cos two sum only works on sorted lists 
        # print(nums)
        for i in range(len(nums)): #outer loop to iterate through list 
            start_pointer = i + 1 #because start value is i itself 
            end_pointer = len(nums) - 1 
            while start_pointer < end_pointer:
                current_total = nums[i] + nums[start_pointer] + nums[end_pointer]
                if current_total == 0:
                    element = [nums[i] , nums[start_pointer] , nums[end_pointer]]
                    if element not in final_result:
                        final_result.append([nums[i] , nums[start_pointer] , nums[end_pointer]])
                    start_pointer += 1 
                    end_pointer -= 1 
                elif current_total > 0:
                    end_pointer -= 1
                elif current_total < 0:
                    start_pointer += 1 
        return final_result
        