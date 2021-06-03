# python3

# You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)

# Output: 7 -> 0 -> 8


class Solution:
    # @param A : head node of linked list
    # @param B : head node of linked list
    # @return the head node in the linked list
    def addTwoNumbers(self, A, B):
        # corner cases
        if A == None and B == None:
            return None
        
        p1, p2 = A, B
        
        # add B to A
        carry = 0
        while p1.next != None and p2.next != None:
            added_num = p1.val + p2.val + carry
            p1.val = added_num%10
            carry = added_num//10
            p1 = p1.next
            p2 = p2.next

        added_num = p1.val + p2.val + carry
        p1.val = added_num%10
        carry = added_num//10

        if p1.next == None and p2.next == None:
            if carry == 1:
                p1.next = ListNode(1)
        else:
            if p1.next == None:
                p1.next = p2.next
            p1 = p1.next
            while carry and p1.next != None:
                added_num = p1.val + carry
                p1.val = added_num%10
                carry = added_num//10
                p1 = p1.next
            if carry == 1:
                added_num = p1.val + carry
                p1.val = added_num%10
                carry = added_num//10
                if carry == 1:
                    p1.next = ListNode(1)
        return A

        

