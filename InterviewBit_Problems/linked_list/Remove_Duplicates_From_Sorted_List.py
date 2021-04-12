# Python

# Given a sorted linked list, delete all duplicates such that each element appear only once.
# For Example,

# Given 1 -> 1 -> 2 return 1 -> 2
# Given 1 -> 1 -> 2 -> 3 -> 3 return 1 -> 2 -> 3

class Solution:
    # @param A: head node of the linked list
    # @return the head node in the linked list.

    def deleteDuplicates(self, A):
        head = A
        while A:
            while A.next and A.next.val == A.val:
                A.next = A.next.next
            A = A.next
        return head

        


