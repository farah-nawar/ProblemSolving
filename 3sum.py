
if __name__ == '__main__':

    n = int(input())
    i,j,k=0,0,0
    for _ in range(1,n+1):
        N = int(input())
        lst = [int(x) for x in input().split()]

        for _ in lst:
            i = lst[i]
            j = lst[j]
            k = lst[k]
            N = lst[i] + lst[j] + lst[k]
            last_digit = int(repr(N)[-1])
            if last_digit == 3:
                print("YES")
            else:
                print("N0")
