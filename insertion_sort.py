n = int(input("enter the array length: "))

arr = [int(input()) for x in range(n)]

print(arr)
key = 0
j = 0

for i in range(1,n):
    key = arr[i]
    j = i - 1

    while(j>=0 and arr[j]>key):
        arr[j+1] = arr[j]
        j = j - 1

    arr[j+1] = key

print(arr)




