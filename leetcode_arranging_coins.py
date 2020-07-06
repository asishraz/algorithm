n = int(input())
left = 0
right = n
mid = 0
k = 0

while left <= right:
    mid = left + (right-left)/2
    k = mid * (mid+1)/2

    if k > n:
        right = mid - 1
    elif k < n:
        left = mid + 1
    else:
        print(int(mid))


print(int(right))    
