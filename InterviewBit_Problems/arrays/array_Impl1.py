#Python3

# What will be the output:
def performOps(A):
    blen = 2*len(A) # will create a space twice the length of array A
    B = [0]*blen    # will create space twice the length of array A, assign all of them value '0'

    for i in range(len(A)):
        B[i] = A[i]  # will copy values of A[i] into B[i], upto length of A.length in B.
        # A = [5, 10, 2, 1]
        # B = [5, 10, 2, 1, 0, 0, 0, 0]

        # for rest of values, this steps assign values by evaluating stmnt
        B[i + len(A)] = A[(len(A) - i) % len(A)]

    return B 

        # This will give values as:
        # A[(4-0) % 4] = A[0] = 5  , 4%4 = 0
        # A[(4-1) % 4] = A[3] = 1  , 3%4 = 3
        # A[(4-2) % 4] = A[2] = 2  , 2%4 = 2
        # A[(4-3) % 4] = A[1] = 10  , 1%4 = 1

B = performOps(A)
for i in range(len(B)):
    print B[i]
