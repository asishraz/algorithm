ls = [2,3,6,6,5]

print(ls)


for i in range(0,len(ls)-1):
    for j in range(0,len(ls)-1-i):
        if ls[j] > ls[j+1]:
            ls[j+1], ls[j] = ls[j], ls[j+1]


print(ls)