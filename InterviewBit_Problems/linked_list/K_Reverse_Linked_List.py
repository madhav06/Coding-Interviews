# Python3

Given a singly linked list and an integer K, reverse the nodes of the list K at a time and return modified linked list.append

For example, Given linked list 1 -> 2 -> 3 -> 4 -> 5 -> 6 and K = 2
it should return 2 - > 1 -> 4 -> 3 -> 6 -> 5.and

# Definition of singly linked-list
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param A: head node of linked list
    # param B: integer
    # @return the head node in the linked list

    def reverseList(self, A, B):
        prev = None
        nex = None
        curr = A

        count = 0

        while count < B:
            nex = curr.next
            curr.next = prev
            prev = curr
            curr = nex

        if nex:
            A.next = self.reverseList(nex, B)
        return prev
        