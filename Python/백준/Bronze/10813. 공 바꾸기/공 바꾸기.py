a, b = map(int,input().split())
arr = [x for x in range(1, a+1)]
for i in range(b):
    a, b = map(int,input().split())
    arr[a-1],arr[b-1] = arr[b-1],arr[a-1]
print(*arr)