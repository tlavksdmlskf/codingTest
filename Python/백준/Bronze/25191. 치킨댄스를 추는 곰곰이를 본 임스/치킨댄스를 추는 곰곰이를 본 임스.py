a = 0
n = int(input())
m = list(map(int,input().split()))

for _ in range(n):
    if(m[0] >= 2):
        m[0] -= 2
        a += 1
    elif(m[1] >= 1):
        m[1] -= 1
        a += 1
print(a)