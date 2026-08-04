class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        best = 0 # initialise best counter
        left = 0 # left window pointer 
        charSet = set()

        for right in range(len(s)):
            while s[right] in charSet:
                charSet.remove(s[left])
                left += 1 
            charSet.add(s[right])
            best = max(best,right-left+1)
        return best 