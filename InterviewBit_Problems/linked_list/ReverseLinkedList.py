# Python3

# Reverse a linked list. Do it in-place and in one-pass.

# For example:
# Given 1->2->3->4->5->NULL,

# return 5->4->3->2->1->NULL.

# class ListNode:
class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def reverseList(self, A):
        cur = A
        prev = None
        while(cur):
            fut = cur.next
            cur.next = prev
            prev = cur
            cur = fut
        return prev
