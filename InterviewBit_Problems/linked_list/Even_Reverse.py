# Python3

'''
Problem Constraints: 1 <= size of LL <= 10 ^ 5

Given a linked list A, reverse the order of all nodes at even positions.

Input format: first and only arg is the head of the Linked list A.

Output format: return the head of the new linked list.

eg
Input: 1 -> 2 -> 3 -> 4
Output: 1 -> 4 -> 3 -> 2

Input: 1 -> 2 -> 3
Output: 1  -> 2 -> 3
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def solve(self, A):
        p = A
        count = 0
        while p:
            p = p.next
            count += 1

        c = [0]*count
        p = A
        i = 0
        while p:
            c[i] = p.val
            p = p.next
            i += 1
        
        if count <= 3:
            return A
        else:
            p = A
            q = A

            if count%2 == 0:
                count = count-1
                while count > 0:
                    p.next.val = c[count]
                    count -= 2
                    p = p.next.next
            
            else:
                count = count - 2
                while count > 0:
                    q.next.val = c[count]
                    count -= 2
                    q = q.next.next
        
        return A

        

