a = list(map(int,input().split()))
hbg = 0
while True:
    if(a[0] < 2 or a[1] < 1):
        break
    a[0] -= 2
    a[1] -= 1
    hbg += 1
print(hbg)