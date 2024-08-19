n = list(map(int,input().split()))

a = [0 for x in range(n[1])] + [1 for x in range(n[0] - n[1])]
b = [0 for x in range(n[2])] + [1 for x in range(n[0] - n[2])]

cnt = 0

for i in range(n[0]):
    if a[i] == b[i]:
        cnt += 1

print(cnt)

