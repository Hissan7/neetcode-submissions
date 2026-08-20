import heapq

class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:

        if len(stones) == 1:
            return stones[0]
        
        # create a max heap
        maxHeap = [] 

        for stone_weight in stones:
            heapq.heappush(maxHeap,-stone_weight)
        print(f"maxHeap before while : {maxHeap}")

        while maxHeap:
            y = -1 * heapq.heappop(maxHeap) #1st stone 
            
            x = -1 * heapq.heappop(maxHeap) # 2nd stone
            print(f"x stone = {x} | y stone = {y}")
            if x == y:
                print(f"x ({x}) is the same as y ({y})")
                print(f"maxHeap after x==y : {maxHeap}")
                pass
            elif x < y:  # neg version of if x < y
                print(f"x ({x}) < y ({y})")
                y -= x 
                print(f"y stone is now {y}")
                heapq.heappush(maxHeap,-y)
                print(f"maxHeap after x<y : {maxHeap}")
            if len(maxHeap) == 1:
                print("the length of maxheap is 1")
                return -1 * maxHeap[0]
        return 0 
            
        


