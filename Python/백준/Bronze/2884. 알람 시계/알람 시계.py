a = list(map(int,input().split()))

if a[1] - 45 < 0:
    print((a[0]-1 if a[0] != 0 else 23), (a[1]+60)-45)
else:
    print(a[0], a[1]-45)