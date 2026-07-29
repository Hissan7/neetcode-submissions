class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        count = 1
        starting_points = []
        s = set()
        if len(nums) == 0:
            return 0
        for element in nums: # add all elements into set 
            s.add(element)
        for element in s:
            if element-1 not in s: #starting point logic
                starting_points.append(element)
        for sp in starting_points:
            current = sp
            length = 1  # the starting point itself counts as length 1
            while (current + 1) in s: #if element+1 is in the set
                current += 1
                length += 1
                print(length)
            if length > count:
                count = length
        return count
            