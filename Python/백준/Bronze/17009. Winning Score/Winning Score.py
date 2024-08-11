a = []

for _ in range(6):
    a.append(int(input()))

if (a[0] * 3) + (a[1] * 2) + (a[2] * 1) > (a[3] * 3) + (a[4] * 2) + (a[5] * 1):
    print("A")
elif (a[0] * 3) + (a[1] * 2) + (a[2] * 1) == (a[3] * 3) + (a[4] * 2) + (a[5] * 1):
    print("T")
else:
    print("B")