




def miniMaxSum(arr):
    x=[]
    for i in range(0,len(arr)):
     y = sum(arr, len(arr) - i)
     x.append(y)

     return min(x) + max(x)



if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)

