# Python3 Code

'''
Given a linked list, return the node where the cycle begins, if no cycle return null.

Example - 
Input : 

                  ______
                 |     |
                 \/    |
        1 -> 2 -> 3 -> 4

Return the node corresponding to node 3. 
'''

# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the first node in the cycle in the linked list
    def detectCycle(self, A):
        if not A: return None
        slow = fast = A
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast: break
        
        if slow != fast: return None
        slow = A
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow