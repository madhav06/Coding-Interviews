# # Python3

# Given a linked list, remove the nth node from the end of the list and return its head.

# for e.g,

# Given Linked List: 1 -> 2 -> 3 -> 4 -> 5 and n = 2

# n = 2 points out that from end of list, we need to remove node at second position.

# after removing the second node from the end, the linked list becomes: 1 -> 2 -> 3 -> 5.

# Definition of single linked list:

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param A: head node of linked list
    # @param B: integer
    # @return the head node in the linked list

    def removeNthFromEnd(self, A, B):

        node = A
        length = 0
        while node is not None:
            length = length + 1
            node = node.next

        if length == 1: return None
        headNode = A
        if B >= length: return headNode.next

        curr = A
        prev = None

        for i in range(length - B):
            prev = curr
            curr = curr.next
            # if curr is None:
            # return headNone.next

        prev.next = curr.next
        return headNode

