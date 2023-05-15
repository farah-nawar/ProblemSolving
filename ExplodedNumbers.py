
lst=[]
n = int(input())
x = [int(x) for x in input().split()]
for i in range(0,n) :
    if i<0:
        i+=1;
        lst.append(i)
    else:
        lst.append(i)
print(*lst)

