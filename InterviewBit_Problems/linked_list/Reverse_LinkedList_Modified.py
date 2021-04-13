'''
Reverse a linked list from position m to n. Do it in-place and in one-pass.

For example:
Given 1->2->3->4->5->NULL, m = 2 and n = 4,

return 1->4->3->2->5->NULL.
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, A, m, n):
        if m == n:
        	return A
        start = end = head = ListNode(0)
        head.next = A
        count_m = m
        while count_m:
            count_m -=1
            prev_1 = start
            start = start.next
            end = end.next
        n-=m
        prev = start
        end = start.next
        while n:
            n-=1
            next = end.next
            end.next = prev
            prev = end
            end = next
        prev_1.next = prev
        start.next = next
        return head.next