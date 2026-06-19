class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        temp = "" #create an empty string 
        temp = ''.join(str(digit) for digit in digits)
        int_l = int(temp) + 1 #plus one to the integer version
        return list(str(int_l))