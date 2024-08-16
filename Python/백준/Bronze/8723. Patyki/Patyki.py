a = sorted(list(map(int,input().split())))

if a[0] == a[1] and a[1] == a[2]:
    print(2)
elif pow(a[0], 2) + pow(a[1], 2) == pow(a[2], 2):
    print(1)
else:
    print(0)