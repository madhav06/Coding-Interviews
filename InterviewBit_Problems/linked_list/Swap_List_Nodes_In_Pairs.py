# python3

'''
Given a linked list, swap every two adjacent nodes and return its head
for example,
Given 1 -> 2 -> 3 -> 4, you should return 2 -> 1 -> 4 -> 3

Your algorithm should use only constant space. you may not modify the values in the list, only nodes itself can be changed.
'''

# Definition of singly linked list:
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param A: head node of linked list
    # @return the head node in the linked list.

    def swapPairs(self, A):

        head = ListNode(None)
        head.next = A
        prev = head
        curr = A

        while curr and curr.next:
            prev.next = curr.next
            curr.next = curr.next.next

            prev.next.next = curr
            prev = curr
            curr = curr.next
            
        return head.next
        

    
