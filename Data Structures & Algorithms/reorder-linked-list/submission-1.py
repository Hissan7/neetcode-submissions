# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        second_list_head = slow.next
        slow.next = None
        prev = None  
        current = second_list_head 
        while current: 
            next_node = current.next 
            current.next = prev
            prev = current
            current = next_node
        second_list_head = prev 
        first_list_pointer = head
        second_list_pointer = second_list_head
        while first_list_pointer and second_list_pointer:
            first_next = first_list_pointer.next  
            second_next = second_list_pointer.next  
            first_list_pointer.next = second_list_pointer   
            second_list_pointer.next = first_next                       
            first_list_pointer = first_next     
            second_list_pointer = second_next  