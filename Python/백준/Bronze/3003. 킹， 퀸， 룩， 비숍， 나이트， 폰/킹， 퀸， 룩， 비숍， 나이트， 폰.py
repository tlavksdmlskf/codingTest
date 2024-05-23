a = list(map(int,input().split()))
setting = [1,1,2,2,2,8]
for i in range(len(setting)):
    setting[i] = setting[i] - a[i]

print(*setting)