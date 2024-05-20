arr = [0 for x in range(int(input()))]
arr[:] = map(int,input().split())

sum = 0
for i in range(len(arr)):
    sum += (arr[i] / max(arr)) * 100
print(sum / len(arr))