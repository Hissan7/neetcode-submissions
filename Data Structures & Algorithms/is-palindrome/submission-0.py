class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        # declare new string 
        new_s = ""
        for char in s:
            if char.isalnum(): #if the char is alnum, add it to the empty string
                new_s += char 
        #check if the string is the same as it's reversed version (palindrome)
        return new_s == new_s[::-1] #(new_S[]::-1] is the reversed version)