a, b = map(int,input().split())
arr = [x + 1 for x in range(a)]
for i in range(b):
    a, b = map(int,input().split())
    arr[a - 1 : b] = reversed(arr[a - 1 : b])
print(*arr)
