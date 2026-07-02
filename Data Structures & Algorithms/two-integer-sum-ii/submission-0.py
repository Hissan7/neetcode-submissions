class Solution:
    def twoSum(self,numbers: list[int], target: int) -> list[int]:
        """
        two pointer 
        1.) what we can do is have a pointer (p1) at the start and a pointer (p2) at the end 
                we need to reate pointers of the indexes not the values 
        2.) p1 goes from left to right and p2 goes from right to left 
        3.) the way to verify there is no solution is to know when p1 or p2's index is the same ???


        p1 starts from left. p2 starts from right. 
        check if p1 + p2 = target
        if not then p1 moves left and p2 moves right 
        check if p1 + p2 = target
        if not then again p1 moves left and p2 moves right 
        repeat until positions of pointers go past midpoint or target is found 
        """

        pointer_start = 0
        pointer_end = len(numbers)-1      
        result = []
        for _ in range(0,len(numbers)):
            if pointer_start < pointer_end and numbers[pointer_start] + numbers[pointer_end] > target:
                pointer_end -= 1
            elif pointer_start < pointer_end and numbers[pointer_start] + numbers[pointer_end] < target:
                pointer_start += 1
            elif pointer_start < pointer_end and numbers[pointer_start] + numbers[pointer_end] == target:
                 result.append(pointer_start+1)
                 result.append(pointer_end+1)
                 return result 

            else:
                 return -1 
                

