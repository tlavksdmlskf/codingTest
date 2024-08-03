a = list(map(int,input().split()))
print(0 if 100 <= a[0] - (a[0] * a[1] / 100) else 1)