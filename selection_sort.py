n = int(input("enter the length of the array: "))

arr = [int(input()) for x in range(n)]


print(arr)

min = 0

for i in range(0,n-1):
    min = i
    for j in range(i+1,n):
        if arr[j] < arr[min]:
            min = j

    arr[i], arr[min] = arr[min], arr[i]
    print(arr)