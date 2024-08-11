c = 9999

for _ in range(int(input())):
    a, b = map(int,input().split())

    if a <= b:
        if b < c:
            c = b

if c == 9999:
    print(-1)
else:
    print(c)