class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count = 0 
        for credential in details:
            if int(credential[11:13]) > 60:
                count += 1 
        return count 
            