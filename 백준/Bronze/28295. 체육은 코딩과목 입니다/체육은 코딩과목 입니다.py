a = 0

for _ in range(10):
    n = input()
    
    if n == '1':
        a += 90
    elif n == '2':
        a += 180
    elif n == '3':
        a -= 90

if a%360 == 0:
    print("N")
elif a%360 == 90:
    print("E")
elif a%360 == 180:
    print("S")
else:
    print("W")