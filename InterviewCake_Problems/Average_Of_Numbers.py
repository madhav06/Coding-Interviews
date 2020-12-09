# Python3

# Python Program to calculate Average of Numbers:

n = int(input("Enter total numbers to be inserted: "))
a = []

for i in range(0,n):
    num = int(input("Enter number: "))
    a.append(num)
    avg = sum(a) / n
    # final = avg // 2
print("Average of numbers: ", round(avg,2))