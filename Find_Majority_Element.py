# python3

def majorityElement(A):

	dict = {}

	for i in A:
		dict[i] = dict.get(i,0) + 1

		for key, value in dict.items():
			if value > len(A) / 2:
				return key

		return -1

if __name__ == '__main__':

	A = [1, 8, 7, 4, , 1, 2, 2, 2, 2, 2, 2]

	res = majorityElement(A)
	if res != -1:
		print("Majority element is", res)
	else:
		print("Majority element does not exist")