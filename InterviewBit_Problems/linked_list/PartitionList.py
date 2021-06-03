# Python3

# Problem Stmnt:

# Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

# You should preserve the original relative order of the nodes in each of the two partitions.

# For example,
# Given 1->4->3->2->5->2 and x = 3,
# return 1->2->2->4->3->5.

class Solution:
    def partition(self, A, B):

        head = ListNode(None)
        head.next = A

        end = []
        cur_node = head

        while cur_node.next != None:
            last_node = cur_node;
            cur_node = cur_node.next;

            if cur_node.value >= B:
                last_node.next = cur_node.next;
                end.append(cur_node.val)

            else:
                tail = cur_node;
        
        for i in end:
            x = ListNode(i)
            tail.next = x
            tail = x
        
        tail.next = None

        return head.next