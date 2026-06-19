class Solution:
    def hammingWeight(self,n: int) -> int:
        count = 0
        x = str(bin(n))
        x_stripped = x[2:]
        for char in x_stripped:
            if char == "1":
                count += 1
        return count