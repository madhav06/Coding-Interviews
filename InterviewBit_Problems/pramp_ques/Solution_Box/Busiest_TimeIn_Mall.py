# Python3

# Mock Interview Scheduled

def find_busiest_period(data):

	people , max_time, max_people = 0,0,0


    # ITERATEING thru indexes of nested array
	for i in range(len(data)):
		# set j to  value of i
		j = data[i]
        
        # if third ele == 1, add index 1 to people
		if j[2] == 1:
			people += j[1]
		else:
			people -= j[1]

		if i == len(data)-1 or data[i][0] != data[i+1][0]:

			if people > max_people:

				max_people = people

				max_time = j[0]

return max_time