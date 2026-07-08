class Solution:
    def encode(self,strs: list[str]) -> str:
        result = ""
        for string in strs: # iterating through "hello world" and "foo" 
            length = str(len(string))
            x = length + "#" + string # "11" + "#" + "hello world"
            # print(f"x: {x}") 
            result += x 
        return result

    def decode(self,s: str) -> list[str]:
        result = []
        i = 0
        while i < len(s):
            j = s.find("#",i) #find index at which # start
            length_str = s[i:j] #find the length of the actual string (which is the number before the #)
            length = int(length_str) #convert to int
            word = s[j+1:j+1+length]
            result.append(word)
            i = j + 1 + length
        return result
