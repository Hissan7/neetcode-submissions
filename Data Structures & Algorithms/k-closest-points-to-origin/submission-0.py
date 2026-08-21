import heapq
import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        maxHeap = []
        res = []

        # 1.) iterate through each list element in the list (list of lists)

        for coords in points: 
        # 2.) calculate the euclidean distance 
            euclidean_distance = math.sqrt(((coords[0] - 0) ** 2) + ((coords[1] - 0) ** 2))
        # 3.) push that val into a minHeap 
            heapq.heappush(maxHeap,(-euclidean_distance,coords))
        # 4.) heapify the heap 
        heapq.heapify(maxHeap)

        while len(maxHeap) > k:
            heapq.heappop(maxHeap)
        
        for tup in maxHeap:
            res.append(tup[1])
        
        return res



        
        