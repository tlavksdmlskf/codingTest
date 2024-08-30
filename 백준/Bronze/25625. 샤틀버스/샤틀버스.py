a = list(map(int, input().split()))

if a[0] > a[1]:
    print(sum(a))
else:
    print(a[1] - a[0])