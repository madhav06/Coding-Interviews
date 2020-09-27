# Problem:  Given an integer array, one element occurs even number of times and all other have odd occurances,
 # find the element with even occurances.


def even_occuring_element(arr):
	""" Returns the even occuring element within the list of integers """

	dict = {}
	for num in arr:

		if num in dict:
			dict[num] += 1
		else:
			dict[num] = 1


	for num in dict:

		if not dict[num] & 1:   # bitwise check for parity
			return num