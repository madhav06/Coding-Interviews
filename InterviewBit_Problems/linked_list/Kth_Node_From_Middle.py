# Python3

'''
Given a linked list A, of length N and an integer B.

You need to find the value of the Bth node from the middle
towards the beginning of the Linked List A.

if no such ele exists, then return -1.



Problem Constraints:
 1 <= N <= 10 ^ 5
 1 <= Value in Each Link List Node <= 10 ^ 3
 1 <= B  <= 10 ^ 5

 Input: First arg is the head pointer of the linked list A,
 Second arg is an int B

 Output: return an int denoting value of the Bth from the middle
 towards the head of the linked list A, if no such ele exists,
 then return -1.



Input: 
 A = 3 -> 4 -> 7 -> 5 -> 6 -> 1 6 -> 15 -> 61 -> 16
 B = 3

Output: 4



Input:
 A = 1 -> 14 -> 6 -> 16 -> 4 -> 10
 B = 2

Output: 14
'''

# Definition for singly-linked list
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param A: head node of the linked list
    # @param B: int
    # @return int

    def solve(self, A, B):
        n = 0
        C = A

        while C is not None:
            n, C = n+1, C.next

            middle = (n//2) + 1
            middleNode = A

            while middle > 1:
                middle, middleNode = middle-1, middleNode.next
                prev = None

                cur = A
            while cur is not None:
                temp = cur.next
                cur.next = prev
                prev = cur
                cur = temp

            while middleNode is not None and B > 0:
                B == 1
                middleNode = middleNode.next

            if middleNode is None:
                return -1
            else:
                return middleNode.val




