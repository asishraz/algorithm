ls = [2,3,33,11,53,1,41,53,32,42,23,42,4,1,3,4,24,34,45,43]

#if target is in the above list or not

target = 44

#linear search
def linearSearch(ls,target):
    for i in range(len(ls)):
        if ls[i] == target:
            print(str(target) + " is in the list ")
            return True
    return False
##print(linearSearch(ls,target))



#binary search
def binarySearch(ls,target):
    ls.sort()
    print(ls)
    low = 0
    high = len(ls)-1
    while low <= high:        
        mid = (low+high) // 2
        if target == ls[mid]:
            return True
        elif target < ls[mid]:
            high = mid - 1
        elif target > ls[mid]:
            low = mid + 1
    return False


print(binarySearch(ls,target))
