# Python3

# Merge two sorted linked lists and return it as new list.

# The new list should be made by slicing together the nodes of the first two lists, and should also be sorted.__init__

# for example, given are two linked lists: 
#     5 -> 8 -> 20
#     4 -> 11 -> 15

# the merged list should be:

#     4 -> 5 -> 8 -> 11 -> 15 -> 20

# Definition for singly linked-list:
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A: head node of linked list
    # @param B: head node of linked list
    # @return the head node in the the linked list

    def mergeTwoLists(self, A, B):
        #head = None
        if A.val <= B.val:
            root = ListNone(A.val)
            A = A.next
        else:
            root = ListNode(B.val)
            B = B.next
        head = root

        while(A or B):
            if A and B:
                if A.val <= B.val:
                    head.next = ListNode(A.val)

                    A = A.next
                else:
                    head.next = ListNode(B.val)

                    B = B.next
            elif(A):
                head.next = ListNode(A.val)

                A = A.next
            else:
                head.next = ListNode(B.val)
                B = B.next
        return root
