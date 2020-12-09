# Python3
# Python program to swap the first values with last values of a list.

newList = []

n = int(input("Enter total numbers in list: "))
for x in range(0,n):
    element = input("Enter number: ")
    newList.append(element)
    print("The list is: ", newList)

newList[0], newList[-1] = newList[-1], newList[0]

print("The swapped list is: ", newList)
