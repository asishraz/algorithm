ls = [2,3,33,11,53,1,41,53,32,42,23,42,4,1,3,4,24,34,45,43]

#if target is in the above list or not

target = 53

#linear search
def linearSearch(ls,target):
    for i in range(len(ls)):
        if ls[i] == target:
            print(str(target) + " is in the list ")
            return True
    return False



print(linearSearch(ls,target))
