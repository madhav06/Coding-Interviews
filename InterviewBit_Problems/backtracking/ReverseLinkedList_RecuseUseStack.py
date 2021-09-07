# Backtracking - if the current solution is not suitable,
# then eliminate that and backtrack (go back) and
# check for other solutions.

# Reverse Linked List Recursion Using Stack

# Python code for the above approach

# Definition for singly-linked list.
class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next


class Solution:

	# Program to reverse the linked list
	# using stack
	def reverseLLUsingStack(self, head):
		
		# Initialise the variables
		stack, temp = [], head
		
		while temp:
			stack.append(temp)
			temp = temp.next

		head = temp = stack.pop()
		
		# Untill stack is not
		# empty
		while len(stack) > 0:
			elem = stack.pop()
			temp.next = elem
			temp = elem

		elem.next = None
		return head


# if __name__ == "__main__":
# 	head = ListNode(1, ListNode(2, ListNode(3,
# 						ListNode(4, ListNode(5)))))
# 	obj = Solution()
# 	head = obj.reverseLLUsingStack(head)
# 	while head:
# 		print(head.val, end=' ')
# 		head = head.next



