# Python3

'''
Given a list , rotate the list to the right by k places, where k is non-negative
for example,

Given: 1 -> 2 -> 3 -> 4 -> 5 -> Null, K = 2,
return 4 -> 5 -> 1 -> 2 -> 3 -> Null.

'''

# definition of singly linked list:

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param A: head node of linked list
    # @param B: integer
    # @return the head node in the linked list

    def rotateRight(self, A, B):
        head = A
        last = None
        length = 0

        # get length of list as well as the last node of the current list
        while A:
            last = A
            A = A.next
            length += 1
        
        # because B can be greater than length of list... normalize it
        B %= length

        if B == 0:
            return head
        curr = head

        # get to the point where we will detach the list and rotate it

        for i in range(length - B - 1):
            curr = curr.next

        rotate_head = curr.next
        curr.next = None
        last.next = head

        return rotate_head