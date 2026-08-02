# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    # def reverse(head):
    #     prev = None
    #     current = head
    #     while current:
    #         next_node = current.next
    #         current.next = prev
    #         prev = current
    #         current = next_node
    #     return prev

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        N = 0 # count to record when we hit the node before the d_node
        current = head
        while current: #traverse through list and increment counter 
            N += 1
            current = current.next
        print(f"The length of the linked list is {N}")
        target_node_position = N - n
        print(f"N ({N}) - n ({n}) = {target_node_position}")
        traversal_count = 0 
        current = head # reset traversal
        while current and traversal_count < target_node_position - 1:
            traversal_count += 1 
            current = current.next
        if target_node_position == 0:
            return current.next
        current.next = current.next.next
        return head 

        
        # need to think of a way to traverse the list 
        # point the target node to null
        # point node before target node to node after the target node. 
        # return the head 

















        # the strat im thinking of right now 
        # since we need to remove the n'th node FROM THE END OF THE LIST
        # first we can reverse the list 
        
        # once the list is reversed, traverse through list until the nth node is reached
        # disconnect that node (this diconnected node lets call it d_node)
        # the node before d_node needs to point to the node after d_node

        
        """
        let n = 1 
        [1,2,3,4]
        first reverse the list so it becomes :
        [4,3,2,1]
        n = 1 so d_node = 3 
        [4,2,1]
        and then the node before d_node (4) needs to point to the node after d_node (2)

        once thats done we reverse it back and return it 

        done ???

        """
        
