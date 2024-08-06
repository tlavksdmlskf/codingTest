a = [0 for _ in range(5)]

for i in range(5):
    a[i] = int(input())

if(a[0] > 0):
    print((a[1] - a[0]) * a[4] )
else:
    print((abs(a[0]) * a[2] )+ a[3] + a[1] * a[4])
    
