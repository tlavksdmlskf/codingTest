m = list(map(int,input().split()))
cnt = (m[1] // m[3]) * (m[2] // m[3])

if(cnt > m[0]):
    print(m[0])
else:
    print(cnt)