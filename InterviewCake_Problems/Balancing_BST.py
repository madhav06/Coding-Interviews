# how to determine is binary tree is balanced?

# Node
class Node(object):
	"""docstring for Node"""
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

	# function to compute height

	def height(root):

		#base condition
		if root is None:
			return 0
		return max(height(root.left), height(root.right)) + 1

	# check if height-balanced or not

	def isBalanced(root):

		#base condition
		if root is None:
			return True

		# for left, right subtree height

		lht = height(root.left)
		rht = height(root.right)

		# allowed values for (lht - rht) are 1, -1, 0
		if (abs(lht - rht) <= 1) and isBalanced(root.left) is True and isBalanced(root.right) is True:
			return True

		return False



# testing
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.left.left = Node(8)

if isBalanced(root):
	print('Tree is balanced')
else:
	print('Tree is not balanced')

# O(n^2) is the Worst Case Complexity, optimized case complexity posting soon.


		