class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        nums_copy = []
        ans = []
        for element in nums:
            nums_copy.append(element)
        nums_copy.extend(nums)
        return nums_copy