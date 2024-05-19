arr = [x for x in range(1,31)]
for i in range(28):
    num = int(input())
    arr[num - 1] = 0
arr.sort()
for i in arr:
    if (i != 0):
        print(i)