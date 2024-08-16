a = list(map(int,input().split()))
b = list(map(int,input().split()))
c = 0

for i in range(3):
    if a[i] < b[i]:
        c += b[i] - a[i]

print(c) 

