# Problem Stmt: 
Sort a linked list in O(n log n) time using constant space complexity.

# I/p: 1 -> 5 -> 4-> 3
# O/p: 1 -> 3 -> 4 -> 5



class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def sortList(self, A):

        L = []
        start = A
        while start:

            L.append(start.val)
            start = start.next

        L.sort()
        start = A

        while L:
            start.val = L.pop(0)
            start = start.next
        return A

        

