# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        current = head
        seen = set() #no duplicates in a set 

        while current:
            if current not in seen: # if the current node isnt in the set 
                seen.add(current) # add to set 
                current = current.next # move onto the next node 
            else:
                return True

        # what do you return if the loop finishes normally?
        # well if the loop finishes normally then there is no duplicate so return false
        return False 