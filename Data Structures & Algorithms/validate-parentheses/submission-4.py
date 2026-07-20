class Solution:
    def isValid(self,s:str) -> bool:
        stack = []
        bracket_dict = { ')':'(' , ']':'[' , '}':'{'}
        for char in s:
            if char in bracket_dict.values():
                print(f"{char} has been appended to stack")
                stack.append(char)
            if char in bracket_dict:
                if stack and stack[-1] == bracket_dict[char]:
                    stack.pop()
                else:
                    return False
        if not stack:
            return True
        return False
                    
