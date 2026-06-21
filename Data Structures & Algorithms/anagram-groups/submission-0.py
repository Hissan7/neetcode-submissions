from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        string_dict = defaultdict(list)
        #iterate through the list of string 
        for string in strs: 
            # because dictionary keys are immutable
            sorted_s = tuple(sorted(string))  
            #the word is mapped to the key of the word which is a tuple of its sorted characters 
            string_dict[sorted_s].append(string) 
        # iterate through the values in the dict and add it to an empty list 
        for value in string_dict.values():
            result.append(value)

        # return a list of lists as expected 
        return result 