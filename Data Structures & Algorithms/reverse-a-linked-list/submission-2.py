# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# [2,3]
# listnode[]

#ListNode(2) = node1
#ListNode(3) = node2

#node1.next = node2

#node2.next = node1
#node1.next = null

# Create individual nodes
#node1 = ListNode(1)
#node2 = ListNode(2)
#node3 = ListNode(3)

# Link them together
#node1.next = node2
#node2.next = node3

# Head of the list
#head = node1


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr:
            temp = curr.next 
            curr.next = prev
            prev = curr 
            curr = temp 
        return prev


        