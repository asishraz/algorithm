A = [8,3,2,5,6,1,7,4,9]
A1 = [2,3,8,5]
A2 = [1,4,6,7,9]
print(A)

i=j=k = 0

m = len(A1)
n = len(A2)

while (i < m and j <n):
    if A1[i] < A2[j]:
        A[k] = A1[i]
        i += 1
        k += 1
    else:
        A[k] = A2[j]
        j += 1
        k += 1

while (i < m):
    A[k] = A1[i]
    i += 1
    k += 1

while (j < n):
    A[k] = A2[j]
    j += 1
    k += 1

print(A)


'''
more algo
'''