length, num = map(int,input().split())
arr = list(map(int,input().split()))

for i in arr:
    if i < num:
        print(i, end=" ")