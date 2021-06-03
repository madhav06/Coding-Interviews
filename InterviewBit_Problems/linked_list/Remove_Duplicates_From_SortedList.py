# Problem number: Remove Duplicates from Sorted List ||

# Problem Stmnt: Given a sorted linked list, delete all nodes that have duplicate numbers, 
# leaving only distinct numbers from the original list.

# for example, 
# Given : 1 -> 2 -> 3 -> 3 -> 4 -> 4 -> 5, return 1 -> 2 -> 5.

# Given : 1 -> 1 -> 2 -> 3 return 2 -> 3.

class Solution:
    # @param A: head node of linked list.
    # @return the head node in the linked list.

    def deleteDuplicates(self, A):
        curr = A
        head = prev = ListNode(None)
        head.next = curr

        while curr and curr.next:
            if curr.val == curr.next.val:
                while curr and curr.next and curr.val == curr.next.val:
                    curr = curr.next

                # still one of duplicate values left so advance
                curr = curr.next
                prev.next = curr

            else:
                prev = prev.next
                curr = curr.next
        return head.next


