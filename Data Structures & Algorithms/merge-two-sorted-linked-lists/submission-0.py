# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode() #create a dummy node 
        tail = dummy #tail points to dummy node

        while list1 and list2: #while list1 and list2 have nodes 
            if list1.val <= list2.val: #if the value of the node in list1 is less than or equal to the value of the node in list2
                tail.next = list1  #attach list1's current node to the end of the merged list 
                list1 = list1.next #progress list1 node
                tail = tail.next #progress tail node
            else:
                tail.next = list2 #tail points to next node in list2
                list2 = list2.next #progress list2 node
                tail = tail.next #progress tail node

        if list1: 
            tail.next = list1
        else:
            tail.next = list2

        return dummy.next