# Python3

'''
Given a singly linked list
L: L0 -> L1 -> ..... Ln-1 -> Ln
reorder it to:

L0 -> Ln -> L1 -> Ln-1 -> L2 -> Ln-2 -> ......

You must do this in place without altering the nodes values.
'''

# Definiton of singly linked list
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = head


class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def reorderList(self, A):
        if A is None or A.next is None:
            return A
        mid, last = A, A
        while last.next is not None:
            last = last.next
            if last.next is not None:
                mid = mid.next
                last = last.next
        reverse_list(mid.next)
        mid.next = None
        
        cur = A
        while cur is not None and last is not None:
            tmp = last.next
            last.next = cur.next
            cur.next = last
            last = tmp
            cur = cur.next.next
        return A

def reverse_list(head):
    prev = None
    while head is not None:
        tmp = head.next
        head.next = prev
        prev, head = head, tmp