# Design a stack which returns the minimum element from the stack in constant time, The stack should be
# supporting all operations like top, push , pop, size etc with no degrade in performance for these ops.

from collections import deque

class MinStack:
	def __init__(self):
		# stack to store element
		self.s = deque()

		# variable to store min ele
		self.min = None

	# Insert ele from top
	def push(self, x):

		if not self.s:
			self.s.append(x)
			self.min = x

		elif x > self.min:
			self.s.append(x)
		else:
			self.s.append(2 * x - self.min)
			self.min = x

		# removes top ele from stack
		def pop(self):

			if not self.s:
				self.print("Stack underflow!")

			top = self.s[-1]
			if top < self.min:
				self.min = 2 * self.min - top
			self.s.pop()

		# returns minimum ele from the stack in constant time
		def minimum(self):