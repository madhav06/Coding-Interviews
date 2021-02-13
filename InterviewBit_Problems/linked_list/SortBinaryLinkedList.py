# python3

# Statement: Given a LinkedList consist of N nodes.

# The LL is binary, that is the data value is either 0 or 1.

# We need to sort the LL and return the new LL.

# Constraints: 1 <= N <= 10 ** 5

# A.val = 0 or A.val = 1

# input: 0 -> 0 -> 1 -> 1 -> 0
# output: 0 -> 0 -> 0 -> 1 -> 1 

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def solve(self, A):
        lastOne=A
        head=A
        while A:
            if lastOne!=None and A.val==0:
                # t=lastOne
                lastOne.val,A.val=A.val,lastOne.val
                lastOne=lastOne.next
            A=A.next
        return head 


