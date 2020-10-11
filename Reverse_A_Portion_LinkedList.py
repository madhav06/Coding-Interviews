# Python3

# A linked list node
class Node:
	def __init__(self, data=None, next=None):

		self.data = data
		self.next = next

# Utility function to print a linked list

def printList(msg, head):
	print(msg, end=': ')
	ptr = head
	while ptr:
		print(ptr.data, end=" -> ")
		ptr = ptr.next
	print("None")

# Iteratively reverse a linked list from position m to n
def reverse(head, m, n):

	prev = None
	curr = head

	# 1. Skipping the first m nodes
	i = 1
	while curr is not None and i < m:
		prev = curr
		curr = curr.next
		i = i + 1

	# prev points to pos (m-1)
	# curr points to mth node

	start = curr
	end = None

	# Traverse and reverse the sub-list
	while curr is not None and i <= n:

		next = curr.next
		curr.next = end
		end = curr

		curr = next
		i = i + 1

	# returning head node
	start.next = curr
	if prev is None:
		head = end
	else:
		prev.next = end
	return head


if __name__ == '__main__':

	head = None
	for i in reversed(range(7)):
		head = Node(i+1, head)


	(m,n) = (2,5)

	printList("Original Linked List", head)
	head = reverse(head, m, n)
	printList("Reversed Linked List", head)


	# time complexity is O(n), and no extra space is used. 
    # Problem statement: reverse specific portion of a linked list.