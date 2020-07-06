n  = int(input())

lists = [int(input()) for x in range(n)]
target = int(input())

first = lists[0]
final_list = []

for i in range(1,len(lists)):
    if first + lists[i] == target:
        final_list.append(first)
        final_list.append(lists[i])

