# Python3

# Mock Interview Scheduled

def find_busiest_period(data):

	people , max_time, max_people = 0,0,0

	for j in range(len(data)):
		# set i 
		i = data[j]

		if i[2] == 1:
			people += i[1]