class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []  # will hold indices

        for i, temp in enumerate(temperatures): #for the index and its corresponding temperature in the temperatures array
            while stack and temp > temperatures[stack[-1]]: #while stack aint empty and current temp in the iteration is more than the temperature value at the top of stack
                stack_top_index = stack.pop() # right now thats 0 
                result[stack_top_index] = i - stack_top_index
            stack.append(i)
        return result 