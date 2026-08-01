# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Step 1: Find the middle of the list
        # Use slow/fast pointers with the condition: while fast.next and fast.next.next
        slow, fast = head, head
        
        # TODO: loop while fast.next and fast.next.next
        #   move slow forward by 1
        #   move fast forward by 2
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        
        # TODO: split the list into two halves
        #   'second' should start at slow.next
        #   cut the connection: slow.next = None
        second_list_head = slow.next
        slow.next = None
        

        # first half starts at 'head', second half starts at 'second'
        # (Step 2 and 3 go here later)

        # Step 2: Reverse the second part of the list 
        prev = None  # previous node points to none 
        current = second_list_head # current node 
        while current: #while there are still nodes to traverse 
            next_node = current.next # traverse 
            current.next = prev
            prev = current
            current = next_node
        second_list_head = prev #now the reversed list's head is prev 

        # Step 3: The merging part 
        # We alternately add the nodes from the two lists to form a full complete list
        first_list_pointer = head
        second_list_pointer = second_list_head
        while first_list_pointer and second_list_pointer:
            first_next = first_list_pointer.next   # save first_list_pointer's original next, BEFORE we overwrite it
            second_next = second_list_pointer.next  # save second_list_pointer's original next, BEFORE we overwrite it
            
            first_list_pointer.next = second_list_pointer   # connect first -> second
            second_list_pointer.next = first_next            # connect second -> (original first.next)
            
            first_list_pointer = first_next     # move first pointer forward
            second_list_pointer = second_next   # move second pointer forward