
if __name__ == '__main__':
    n = int(input())

    lstEven = []
    lstOdd = []
    for i in range(1, n+1):
        if i % 2 == 0:
            lstEven.append(i)
        else:
            lstOdd.append(i)

    print(*lstOdd)
    print(*lstEven)


