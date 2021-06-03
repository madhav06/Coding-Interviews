# Sort a linked list using insertion sort.


# Example :

# Input : 1 -> 3 -> 2

# Return 1 -> 2 -> 3

def insert(pos,a):
    a.next=pos.next
    pos.next=a
class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def insertionSortList(self, A):
        head=ListNode(-2*31)
        while A:
            prev=head
            node=head.next
            while node:
                if node.val>=A.val:
                    break
                prev=node
                node=node.next
            insert(prev,ListNode(A.val))
            A=A.next
        return head.next