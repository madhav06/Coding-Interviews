# python3

'''
Problem Description

Given a linked list A of length N and an integer B.

You need to reverse every alternate B nodes in the linked list A.



Problem Constraints
1 <= N <= 105
1<= Value in Each Link List Node <= 103
1 <= B <= N
N is divisible by B


Input Format
First argument is the head pointer of the linkedlist A.

Second argument is an integer B.



Output Format
Return the head pointer of the final linkedlist as described.

Input 1:
A = 3 -> 4 -> 7 -> 5 -> 6 -> 6 -> 15 -> 61 -> 16
B = 3

Output 1:
7 -> 4 -> 3 -> 5 -> 6 -> 6 -> 16 -> 61 -> 15

Input 2:
A = 1 -> 4 -> 6 -> 6 -> 4 -> 10
B = 2

Output 2: 
4 -> 1 -> 6 -> 6 -> 10 -> 4
'''

# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def solve(self, A, B):
        if not A:
            return None
        prev=None
        temp=A
        for i in range(B):
            nextTemp=temp.next
            temp.next=prev
            prev=temp
            temp=nextTemp
        head=prev
        A.next = temp
        if(temp==None):
            return head
        for i in range(B-1):
            temp=temp.next
        temp.next = self.solve(temp.next,B)
        return head
