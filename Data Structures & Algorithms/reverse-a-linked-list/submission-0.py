# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current = head # head is the entry node
        while current:
            next_node = current.next # snapshot of what the next node is 
            current.next = prev #next node points to the previous node 
            prev = current # previous node is now the current one 
            current = next_node
        return prev
        # initialise a prev variable 
        # while the current node does not point to none, do :
            # the next node is the current nodes pointer
            # detach the current node from the list 
                # current = prev ??? (current node points to none)
        