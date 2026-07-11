class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        while len(stones) > 1: 
            stones.sort()
            print(f"stones : {stones}")
            y = stones[len(stones)-1]
            x = stones[len(stones)-2]
            if x < y:
                y -= x 
                stones.pop()
                stones.append(y)
                stones.remove(x)
                print(f"stones : {stones}")
            elif x == y:
                stones.pop()
                stones.pop()
                print(f"stones : {stones}")
                if not stones:
                    return 0 
        return stones[0]