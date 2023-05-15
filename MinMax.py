
n = int(input())
lst=[int(x) for x in input().split()]
minnum=min(lst)
maxnum=max(lst)
lst.clear()
lst.append(minnum)
lst.append(maxnum)
print(sum(lst))

