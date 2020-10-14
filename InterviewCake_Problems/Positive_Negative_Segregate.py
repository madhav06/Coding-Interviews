# Python3

# Segregate positive and negative integers 
# segregating means - collecting -ve first in the order, then collecting +ve in order.

# Problem:  Given an array consist of positive and negative integers, 
# Segregate them in linear time and constant space. Output prints -ve followed by +ve.


def swap(a, i, j):

	temp = a[i]

	a[i] = a[j]

	a[j] = temp

def partition(a, start, end):

	pIndex = start

	for i in range(start, end + 1):

		if a[i] < 0:

			swap(a, i, pIndex)
			pIndex = pIndex + 1


if __name__ == '__main__':

	a = [8, -3, 5, -2, -7, -6, 1, 3]

	partition(a, 0, len(a) - 1)
	print(a)