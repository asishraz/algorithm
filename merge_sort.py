A=[2,4,1,6,8,5,3,7]

A1 = [1,2,4,6]

A2 = [3,5,7,8]

m = len(A1)
n = len(A2)
i = j = k = 0

while(i<m and j<n):
    if A1[i] < A2[j]:
        A[k] =  A1[i]
        i += 1
        k += 1
    else:
        A[k] = A2[j]
        j += 1
        k += 1

while(i<m):
    A[k] = A1[i]
    i += 1
    k += 1

while(j<n):
    A[k] = A2[j]
    k += 1
    j += 1

print(A)