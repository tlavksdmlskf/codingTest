n = list(map(int,input().split()))
a = int(n[0] * n[1] / n[2])
b = int(n[0] / n[1] * n[2])

print(a if a > b else b)